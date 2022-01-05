from django.urls import path
from .views import student_delete, student_add, student_detail, student_list, student_update

urlpatterns = [
    path('',student_list, name='list'),
    path('add/',student_add, name='add'),
    path('detail/<int:id>',student_detail, name='detail'),
    path('update/<int:id>',student_update, name='update'),
    path('delete/<int:number>',student_delete, name='delete'),
]