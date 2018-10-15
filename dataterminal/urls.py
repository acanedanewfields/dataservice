from django.urls import path
from dataterminal import views

urlpatterns=[
    path('dashboard/',views.index, name='dashboard'),
    path('fieldmap/',views.fieldmap, name='fieldmap'),
    path('study/',views.study, name='study'),
    path('entry/',views.entry, name='entry'),
    path('plot/',views.plot, name='plot'),
    path('obs/',views.obs, name='obs'),
    path('qc/',views.qc, name='qc'),
    path('qc_obs/',views.qc_obs, name='qc_obs'),
]