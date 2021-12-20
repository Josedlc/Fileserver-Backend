from django.urls import path, include
from rest_framework import routers  
from .views import *
# import everything from views
  
# define the router
router = routers.DefaultRouter()
  
# define the router path and viewset to be used

router.register(r'department', DepartmentViewSet)
router.register(r'fileup', FileUpViewSet)
router.register(r'', FileViewSet)

# URLS
urlpatterns = [
    path('', include(router.urls)),
   # path('view', FileView.as_view()),
]