from django.shortcuts import render

from Flux.models import Ticket
# from django.http import HttpResponse

# def review(request):
#     r_tickets = Ticket.objects.all()
#     return render(request,"flux/flux.html",
#      {'r_ticket':r_tickets[3]})

def ticket(request):
    tickets = Ticket.objects.all()
    return render(request,"flux/flux.html", 
    {'all_tickets':tickets})