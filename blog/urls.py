from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', views.home, name='home'),
      path('', RedirectView.as_view(url='/projects/')),
]