from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views import generic
from .models import Tarea
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator

from django.conf import settings
from io import BytesIO
from reportlab.pdfgen import canvas
from django.views.generic import View
from django.http import HttpResponse

class StaffRequiredMixin(object):
    
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

# Create your views here.
class HomePageView(TemplateView):
    template_name = "home.html"

@method_decorator(staff_member_required, name='dispatch')
class TareaListView(generic.ListView):
    model = Tarea
    template_name = "index.html"

@method_decorator(staff_member_required, name='dispatch')
class TareaDetailView(generic.DetailView):
    model = Tarea
    template_name = "detalle.html"

@method_decorator(staff_member_required, name='dispatch')
def primer_reporte(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachament: filename=Primer-Reporte.pdf'
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)

    c.setLineWidth(.3)
    c.setFont('Helvetica', 22)
    c.drawString(30,750,'Reporte')
    c.setFont('Helvetica', 12)
    c.drawString(30,735,'Primero')

    c.setFont('Helvetica-Bold', 12)
    c.drawString(480,750,'19/11/2019')
    c.line(460,747,560,747)

    c.save()
