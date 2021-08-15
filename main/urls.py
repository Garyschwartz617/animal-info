from django.urls import path

from .views import homepage,family,animal

urlpatterns = [
    
    path('', homepage),
    path('family/<int:num>', family),
    path('animal/<int:num>', animal)
    # path('about',about)
]
