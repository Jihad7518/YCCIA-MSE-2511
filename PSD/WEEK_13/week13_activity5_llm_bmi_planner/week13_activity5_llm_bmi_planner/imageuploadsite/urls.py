from django.urls import path
from planner import views

urlpatterns = [
    path('', views.plan_page, name='plan'),
]
