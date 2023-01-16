from django.urls import path
from . import views # importing views module from current folder

app_name = "todo_app"

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:task_id>', views.delete, name='delete'),
    path('edit/<int:task_id>', views.edit, name='edit'),
    path('cbvhome/', views.TaskListView.as_view(), name='class_based_list_view'),
    path('cbvdetail/<int:pk>', views.TaskDetailView.as_view(), name='class_based_detail_view'),
    path('cbvupdate/<int:pk>', views.TaskUpdateView.as_view(), name='class_based_update_view'),
    path('cbvdelete/<int:pk>', views.TaskDeleteView.as_view(), name='class_based_delete_view')
]