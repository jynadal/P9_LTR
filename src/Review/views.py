from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from Review.models import Review, Ticket
from Review.forms import reviewForm, ticketForm


# CRUD
@login_required
def ticket_create(request):
    form = ticketForm()
    if request.method =='POST':
        form = ticketForm(request.POST, request.FILES)
        ticket = form.save(commit=False)
        ticket.user = request.user
        # here add ticket.image=request.image
        ticket.save()
        return redirect("flux/")
    return render(request, 'review/ticket_create.html', {'form':form})

@login_required
def ticket_and_review_create(request):
    review_form = reviewForm()
    ticket_form = ticketForm()
    if request.method == 'POST':
        review_form = reviewForm(request.POST)
        ticket_form = ticketForm(request.POST)#,request.FILES
        if any([review_form.is_valid(),ticket_form.is_valid()]):
            ticket = ticket_form.save(commit=False)
            ticket.title = request.title
            ticket.user = request.user
            # here add ticket.image=request.image
            ticket.save()

            review = review_form.save(commit=False)
            review.user = request.user
            review.ticket = ticket.title
            review.save()
            return redirect('flux')
    context = {
        'review_form': review_form,
        'ticket_form': ticket_form,
}
    return render(request,'review/create_review_ticket.html', context=context)

@login_required
def view_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    return render(request,'review/view_review.html', {'review':review})       


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


# Equivalant du HOME
@login_required
def review_ticket(request):
    reviews = Review.objects.all()
    tickets = Ticket.objects.all()
    return render(request, 'review/index.html',context={'reviews':reviews, 'tickets':tickets})

# def rt_detail(request):
#     rt_list= Ticket.objects.all()
#     return render(request, 'review/index.html',
#     {'rt_list':rt_list})

@login_required
def rt_detail(request, ticket):
    rt_list= Ticket.objects.get(ticket=ticket)
    return render(request, 'review/ticket.html',
    {'rt_list':rt_list})