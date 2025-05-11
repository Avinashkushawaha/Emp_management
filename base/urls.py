from django.urls import path
from .import views
from django.shortcuts import redirect

urlpatterns = [
    path('home/', views.home, name='home'),
    path('add_emp/', views.add_emp, name='add_emp'),
    path('delete_emp/<int:emp_id>', views.delete_emp, name='delete_emp'),
    path('update_emp/<int:emp_id>', views.update_emp, name='update_emp'),
    path('do_update_emp/<int:emp_id_temp>', views.do_update_emp, name='do_update_emp'),
    path('', lambda request: redirect('home')), 
]   