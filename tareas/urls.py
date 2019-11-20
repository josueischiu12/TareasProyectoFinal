from django.urls import path

from . import views
from django.views.generic import TemplateView

app_name = "tareas"

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path("tareas/", TemplateView.as_view(template_name='tareas.html'), name="tareas"),
    path("tareas/lista", views.TareaListView.as_view(), name="index"),
    path("tareas/detalle/<int:pk>/", views.TareaDetailView.as_view(), name="detalle"),
    path("tareas/reportes/", TemplateView.as_view(template_name='reportes.html'), name="reportes"),
    #path("tareas/reportes/primero/", views.ReporteTareasAsignadasPDF.as_view(), name="primer_reporte"),
]