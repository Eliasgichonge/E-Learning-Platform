from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, \
     UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Course


class OwnerMixin:
      def get_queryset(self):
          qs = super().get_queryset()
          return qs.filter(owner=self.request.user)


class OwnerEditMixin:
      def form_valid(self, form):
          form.instance.owner = self.request.user
          return super().form_valid(form)


class ManageCourseListView(ListView):
      model = Course
      template_name = 'courses/manage/course/list.html'

      def get_queryset(self):
          qs = super().get_queryset()
          return qs.filter(owner=self.request.user)
