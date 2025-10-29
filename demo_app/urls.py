from django.contrib import admin
from django.urls import path, include
from tasks import views  # import your home view

urlpatterns = [
    path('', views.home, name='home'),  # Homepage
    path('admin/', admin.site.urls),
    path('api/', include('tasks.urls')),  # All task-related APIs
]
