from django.contrib import admin
from django.urls import path, include
from Authentication import views

import Review.views
# from Review.models import Review


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    # path('',include('Authentication.urls')),
    path('flux/',Review.views.review, name='review'),
]
