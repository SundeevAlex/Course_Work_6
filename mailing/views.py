from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy, reverse
from mailing.models import Mailing, Client
from mailing.forms import ClientForm
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin


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


class ClientListView(LoginRequiredMixin, ListView):
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


class ClientCreateView(LoginRequiredMixin, CreateView):
    """
    Контроллер отвечающий за создание клиента
    """
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:clients_list')

    def form_valid(self, form):
        client = form.save()
        user = self.request.user
        client.owner = user
        client.save()
        return super().form_valid(form)


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    """
    Контроллер отвечающий за редактирование клиента
    """
    model = Client
    form_class = ClientForm

    def get_success_url(self):
        return reverse_lazy('mailing:clients_list')
        # return reverse('mailing:view', args=[self.kwargs.get('pk')])


class ClientDetailView(LoginRequiredMixin, DetailView):
    """
    Контроллер отвечающий за отображение клиента
    """
    model = Client

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user == self.object.owner or self.request.user.is_superuser:
            return self.object
        raise PermissionDenied


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    """
    Контроллер отвечающий за удаление клиента
    """
    model = Client
    success_url = reverse_lazy('mailing:clients_list')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user == self.object.owner or self.request.user.is_superuser:
            return self.object
        raise PermissionDenied
