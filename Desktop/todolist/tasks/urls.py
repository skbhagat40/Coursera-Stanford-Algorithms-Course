from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'tasks'
urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(),name = 'detail'),
    path('create',views.CreateTask.as_view(),name = 'add_task'),
    path('',views.IndexView.as_view(),name='homepage'),
    path('task/<int:pk>/',views.UpdateTask.as_view(),name = 'update_task'),
    path('task/<int:pk>/delete/',views.DeleteTask.as_view(),name = 'delete_task'),
    ]
