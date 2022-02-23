
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name='index' ),
    path('tasks/',views.tasks, name='tasks' ),
    path('delete/<int:id>',views.delete, name='del' ),
    path('update/<int:id>',views.update, name='del' ),
    
]
