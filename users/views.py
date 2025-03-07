from users.forms import UserRegisterForm
from django.urls import reverse, reverse_lazy
from users.models import User
import secrets
import string
import random
from django.core.mail import send_mail
from django.shortcuts import redirect, get_object_or_404, render
from config.settings import EMAIL_HOST_USER
from django.views.generic import CreateView
from django.contrib.auth.decorators import permission_required


class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email-confirm/{token}/'
        send_mail(subject="Подтверждение почты",
                  message=f"Перейдите по ссылке для подтверждения почты {url}",
                  from_email='airnav@yandex.ru',
                  recipient_list=[user.email]
                  )
        return super().form_valid(form)


def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse('users:login'))


def reset_password(request):
    context = {
        'success_message': 'Пароль был успешно сброшен, новый пароль был отправлен на Ваш адрес электронной почты.',
    }
    if request.method == 'POST':
        email = request.POST.get('email')
        user = get_object_or_404(User, email=email)
        characters = string.ascii_letters + string.digits
        characters_list = list(characters)
        random.shuffle(characters_list)
        password = ''.join(characters_list[:10])

        user.set_password(password)
        user.save()

        send_mail(
            subject='Восстановление пароля',
            message=f'Вы запрашивали обновление пароля. Ваш новый пароль: {password}',
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
        )
        return render(request, 'users/reset_password.html', context)
    return render(request, 'users/reset_password.html')


@permission_required('users.deactivate_user')
def toggle_activity(request, pk):
    user = User.objects.get(pk=pk)
    if user.is_active:
        user.is_active = False
    else:
        user.is_active = True
    user.save()
    return redirect(reverse('users:users_list'))
