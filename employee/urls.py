from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('employees/', views.employee_list),
    path('employee/<int:pk>', views.employee_detail)
]

