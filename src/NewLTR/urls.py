from django.contrib import admin
from django.urls import path, include
from Authentication import views
import Flux.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    # path('',include('Authentication.urls')),
    path('flux',Flux.views.review, name='flux'),
]
