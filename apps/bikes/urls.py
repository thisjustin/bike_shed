from django.urls import path

from apps.bikes import views

app_name = 'bikes'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('bikes/<int:bike_id>/', views.detail, name='detail')
]
