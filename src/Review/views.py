from django.shortcuts import render
from Review.models import Review


def review(request):
    # avis = Review.objects.all()
    return render(request,"review/index.html",
    #  {'avis':avis[3]}
     )