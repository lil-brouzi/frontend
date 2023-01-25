from django.urls import path

from .views import DemendPage, GeographyPage, HomePage, vacancy, SkillsPage


urlpatterns = [
    path('', HomePage, name='home'),
    path('demend/', DemendPage, name='demend'),
    path('geography/', GeographyPage, name='geography'),
    path('skills/', SkillsPage, name='skills'),
    path('vacancy/', vacancy, name='vacancy'),
]