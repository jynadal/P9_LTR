from django import forms
from Review.models import Review, Ticket
from django.conf import settings


class ticketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('title', 'description')
           # '__all__'
    # title = forms.CharField(label='Titre - Auteur', max_length=128)
    # description = forms.CharField(max_length= 2048)
    # user = forms.CharField(max_length=128)
    # image = forms.ImageField()
    # time_created = forms.DateTimeField()


class reviewForm(forms.ModelForm):
    class Meta:
        model = Review
        # model = Ticket
        fields = '__all__'