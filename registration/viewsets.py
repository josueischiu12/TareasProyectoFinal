from rest_framework import viewsets, filters
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from .serializers import UserSerializer, GroupSerializer
from django.views.generic import CreateView
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator

class StaffRequiredMixin(object):
    @method_decorator(staff_member_required)
    def dispath(self, request, *args, **kwargs):
        return super(SingleView, self).dispatch(request, *args, **kwargs)

class SingleView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (filters.SearchFilter,)

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    filter_backends = (filters.SearchFilter,)