from django.urls import path
from mailing.apps import MailingConfig
from mailing.views import HomeView, ClientListView

app_name = MailingConfig.name

urlpatterns = [
    # path('', index, name='index'),
    path('', HomeView.as_view(), name='index'),
    path('clients_list/', ClientListView.as_view(), name='clients_list'),
]
