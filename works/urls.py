from django.urls import path
from . import views

app_name = 'works'

urlpatterns = [
    path('', views.work_list, name='work_list'),
    path(
        '<int:year>/<int:month>/<int:day>/<slug:slug>/', 
        views.work_detail, 
        name='work_detail'
        )
]