from django.shortcuts import redirect, render
from Review.models import Review, Ticket
from Review.forms import reviewForm, ticketForm

# CRUD
def ticket_create(request):
    form = ticketForm()
    return render(request, 'review/ticket_create.html', {'form':form})
def review_create(request):
    formRT = reviewForm()
    return render(request, 'review/review_create.html',{'formRT':formRT})


def review_change(request, id):
    ticket = Review.objects.get(id=id)

    if request.method == 'POST':
        form = reviewForm(request.POST,instance=ticket)
        if form.is_valid():
            #mettre à jour le groupe existant dans la base de données
            form.save()
            # rediriger vers la page détaillée du "ticket" que nous venons de mettre à jouir
            return redirect('review_detail', ticket.id)

    else:
        form = ticketForm(instance=ticket)

    return render(request, 'review/ticket_change.html', {'form':form})

def review_change(request, id):
    review = Review.objects.get(id=id)
    formRT = reviewForm(instance=review)
    return render(request, 'review/review_change.html', {'formRT':formRT})

# def review(request):
#     # critique = Review.objects.all()
#     return render(request,"review/index.html",
#     #  {'avis':avis[3]}
#      )

def review_ticket(request):
    review_list = Review.objects.all()
    return render(request, 'review/index.html',
    {'review_list':review_list })

# def rt_detail(request):
#     rt_list= Ticket.objects.all()
#     return render(request, 'review/index.html',
#     {'rt_list':rt_list})

def rt_detail(request, ticket):
    rt_list= Ticket.objects.get(ticket=ticket)
    return render(request, 'review/ticket.html',
    {'rt_list':rt_list})