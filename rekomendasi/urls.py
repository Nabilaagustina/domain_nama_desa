from django.urls import path
from . import views

urlpatterns = [
    path('', views.form_domain, name='form_domain'),
    path('ajax/kabupaten/', views.get_kabupaten, name='get_kabupaten'),
    path('ajax/kecamatan/', views.get_kecamatan, name='get_kecamatan'),
    path('ajax/desa/', views.get_desa, name='get_desa'),
    path('ajax/domain/', views.get_domain, name='get_domain'),
]
