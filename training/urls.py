from django.urls import path

from . import views

urlpatterns = [
    path('', views.test, name='test'),
    path('result', views.first, name='first'),
    path('adaptive', views.second, name='second'),
    path('final', views.finalgrade, name='final'),
    path('renderpdf', views.generatepdf, name='pdf'),
]