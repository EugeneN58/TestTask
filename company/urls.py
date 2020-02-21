from django.urls import path

from company.views import EmployeeList, EmployeeDetail
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('/employees/', views.employees, name='employees'),
    path('/employees/', EmployeeList.as_view(), name='employees'),
    path('/employees/<int:pk>', EmployeeDetail.as_view(), name='person_detail'),
]
