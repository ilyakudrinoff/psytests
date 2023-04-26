from django.urls import path
from . import views

app_name = 'psytests'

urlpatterns = [
    path('', views.index, name='index'),
    path('child_test/', views.child_test, name='child_test'),
    path('adult_test/', views.adult_test, name='adult_test'),
    path('test/<int:test_id>', views.test, name='test'),
    path('the_end/', views.the_end, name='the_end'),
]
