from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, UpdateView
from django.urls import reverse_lazy, reverse
from mailing.models import Mailing, Client
from mailing.forms import ClientForm

# def index(request):
#     return render(request, 'mailing/index.html')


class HomeView(TemplateView):
    """
    Контроллер главной страницы сайта
    """
    template_name = 'mailing/index.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        mailings = Mailing.objects.all()
        clients = Client.objects.all()
        context_data['all_mailings'] = mailings.count()
        context_data['active_mailings'] = mailings.filter(status=Mailing.STARTED).count()
        context_data['active_clients'] = clients.values('email').distinct().count()

        return context_data


class ClientListView(ListView):
    """
    Контроллер отвечающий за отображение списка клиентов
    """
    model = Client

    def get_queryset(self, queryset=None):
        queryset = super().get_queryset()
        user = self.request.user
        # if not user.is_superuser and not user.groups.filter(name='manager'):
        #     queryset = queryset.filter(owner=self.request.user)
        return queryset


class ClientCreateView(CreateView):
    """
    Контроллер отвечающий за создание клиента
    """
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:clients_list')


class ClientUpdateView(UpdateView):
    """
    Контроллер отвечающий за редактирование клиента
    """
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:clients_list')
    # def get_success_url(self):
    #     return reverse('mailing:view', args=[self.kwargs.get('pk')])
