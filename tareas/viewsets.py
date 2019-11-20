from rest_framework import viewsets, filters
from .models import Tarea
from .serializers import TareaSerializer
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator

class StaffRequiredMixin(object):
    @method_decorator(staff_member_required)
    def dispath(self, request, *args, **kwargs):
        return super(TareaViewSet, self).dispatch(request, *args, **kwargs)

@method_decorator(staff_member_required, name='dispath')
class TareaViewSet(StaffRequiredMixin, viewsets.ModelViewSet):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
    filter_backends = (filters.SearchFilter,)