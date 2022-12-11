from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', views.StudentListCreate.as_view(), name='api'),
    path('api/<int:pk>', views.StudentRetrieveUpdateDestroy.as_view(), name='api'),
]
