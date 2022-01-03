from django.contrib import admin
from django.urls import path, include
# from Authentication import views
import Authentication.views

import Review.views
# from Review.models import Review


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Authentication.views.login_page, name='login'),
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
