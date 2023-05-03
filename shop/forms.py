from django import forms
# from .models import User
from .models import Contact,Tovar

# class UserForm(forms.ModelForm):
#     label = forms.CharField(label='Метка')
#     class Meta:
#         model = User
#         fields = ['label',]

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'message','phone')


class TovarForm(forms.ModelForm):
    class Meta:
        model  = Tovar
        fields = ('name','amount','cost','made_by','description')

