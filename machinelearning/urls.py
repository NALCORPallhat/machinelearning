from django.conf.urls import url, include
from machinelearning.views import hello_world, machine_view, display_machine
urlpatterns = [
    url(r'^hello-world/$', hello_world, name='hello_world'),
    url(r'^machine-learning/$', machine_view, name='machine-learing'),
    url(r'^display-machine/$', display_machine, name='display_machine'),
]