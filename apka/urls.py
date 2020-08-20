from django.urls import path

from apka import views
from apka.views import caly_grafik, nowa_wycieczka, edytuj_wycieczke, usun_wycieczke, lista

urlpatterns = [
    path('caly/', caly_grafik, name="caly_grafik"),
    path('nowy/', nowa_wycieczka, name="nowa_wycieczka"),
    path('edytuj/<int:id>', edytuj_wycieczke, name="edytuj_wycieczke"),
    path('usun/<int:id>', usun_wycieczke, name="usun_wycieczke"),
    path('list/', lista, name='list'),
    path('update_task/<str:pk>/', views.updateTask, name="update_task"),
    path('delete/<str:pk>/', views.deleteTask, name="delete"),

]
