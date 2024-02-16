from django.urls import path
from. import views  # ****SE IMPORTA LA VISTA DE NOMBRE home***


urlpatterns = [
  path('', views.home, name='home'),  # URL para la nueva vista "home"
  path('datos/', views.datos, name='datos'), 
  path('estudio/', views.estudio, name='estudio'), 
  path('recomendacion/', views.recomendacion, name='recomendacion'),
  path('regiones/', views.get_regiones, name='get_regiones'),
  path('hospitales/<int:id_region>', views.get_hospitales, name='get_hospitales'),
  path('hospitales/', views.get_hospitales_v2, name='get_hospitales_v2'),
  path('pacientes/', views.get_pacientes, name='get_pacientes'),
  path('pacientes_h/<int:id_hosp>', views.get_pacientes_hosp, name='get_pacientes_hospital'),
  path('pacientes_r/<int:id_region>', views.get_pacientes_reg, name='get_pacientes_region'),
  
]

