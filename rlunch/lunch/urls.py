from django.conf.urls import url
from . import views
from .models import Talk


urlpatterns = [
    url(r'^talk/$', views.TalkListView.as_view(), name='talk_list'),
    url(
        r'^talk/(?P<pk>[0-9]+)$', views.TalkDetailView.as_view(),
        name='talk_detail'),
    url(
        r'^talk/create/$', views.TalkCreate.as_view(),
        name='talk_create'),
    url(
        r'^talk/update/(?P<pk>[0-9]+)$', views.TalkUpdate.as_view(),
        name='talk_update')
]
