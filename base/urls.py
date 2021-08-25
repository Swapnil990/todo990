from django.urls import path
from .import views
from.views import TaskUpdate, Tasklist,TaskDetail,TaskCreate,TaskUpdate,TaskDelete,CustomLoginView,RegisterPage,TaskReorder
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/',CustomLoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(next_page='login'),name='logout'),
    path('',Tasklist.as_view(),name='tasks'),
    path('task/<int:pk>/',TaskDetail.as_view(),name='task'),
    path('task-create/',TaskCreate.as_view(),name='task-create'),
    path('task-update/<int:pk>/',TaskUpdate.as_view(),name='task-update'),
    path('task-delete/<int:pk>/',TaskDelete.as_view(),name='task-delete'),
    path('register/',RegisterPage.as_view(),name='register'),
    path('task-reorder/',TaskReorder.as_view(), name='task-reorder'),
]
