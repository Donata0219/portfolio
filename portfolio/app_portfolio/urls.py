from django.urls import path
from .views import ProfilisIrProjektaiView

urlpatterns = [
    path('profiliai/', ProfilisIrProjektaiView.as_view(), name='profiliai'),

]






