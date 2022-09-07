from django.urls import path
from django.contrib.auth import views as authViews
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('tasks/<int:pk>/', views.taskDetal, name='task_detale'),
    path('task-uoc', views.uocData, name='task-uoc'),
    path('get-data', views.getData, name='get-data'),
    path('login', views.user_login, name="login"),
    path('logout/', authViews.LogoutView.as_view(next_page="login"), name="logout"),
    path('sorttable', views.sortTable, name="sorttable"),

]
