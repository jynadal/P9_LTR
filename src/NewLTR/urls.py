from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from django.contrib.auth.views import (LoginView, LogoutView,PasswordChangeView, PasswordChangeDoneView)
import Authentication.views

import Review.views
# from Review.models import Review


urlpatterns = [
    path('admin/', admin.site.urls),

    #Authentication
    path('',LoginView.as_view(template_name='authentication/login.html', redirect_authenticated_user=True), name='login'),
    path('logout/',LogoutView.as_view(), name='logout'),
    # path('logout',Authentication.views.logout_user, name='logout'),
    path('change-password/', PasswordChangeView.as_view(template_name='authentication/password_change.html'), name='password_change'),
    path('change-password-done',PasswordChangeDoneView.as_view(template_name='authentication/password_change_done.html'), name='password_change_done'),
    path('signup/',Authentication.views.signup_page, name='signup'),
    # path('',include('Authentication.urls')),


    path('flux/',Review.views.review_ticket, name='review_ticket'),
    # path('flux/',Review.views.rt_detail, name='rt_detail'),
    path('flux/<str:title>',Review.views.rt_detail, name='rt_detail'),
    # path('createTicket/',Review.views.create_ticket, name="create_ticket"),

    #CRUD
    path('flux/add/', Review.views.ticket_create, name="ticket_create"),
    path('flux/addRT/', Review.views.review_create, name="review_create"),
    # path('flux/addRT/', include('ticket_create.urls')),
    # path('flux/changeT/',Review.views.ticket_change, name="ticket_change"),
    # path('flux/changeRT/', Review.views.review_change, name="review_change"),
    

    # path('flux/',Review.views.review, name='review'),
]
