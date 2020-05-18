from django.urls import path, include, re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.index),
    re_path(r'^(\d+)/(\d+)/$', views.detail),
    re_path(r'^grades/$', views.grades),
    re_path(r'^students/$', views.student),
    re_path(r'^grades/(\d+)$', views.grades_students)
]
