from django.conf.urls import url
from accounts import views
from django.contrib.auth.views import login

urlpatterns = [
    url(r'^$', views.home),
    url(r'^login$', login, {'template_name': 'accounts/login.html'}),
    url(r'^logout$', views.logout_view),
    url(r'^register$', views.register),
    url(r'^profile$', views.profile)
    ]