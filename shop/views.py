from django.shortcuts import render
# from .models import User
from .forms import ContactForm,TovarForm
# Create your views here.
# def main_page(request):

#     users = User.objects.all()
#     # new_user = User(name="Asa",second_name="Nusa")
#     # new_user.save()
#     print(users)
#     # for j in range(44,31,-1):
#     # User.objects.get(id=47).delete()

#     if request.method == 'POST':
#         form = UserForm(request.POST)
#         if form.is_valid():
#             label = form.cleaned_data['label']
#             User.objects.create(label=label)
#     else:
#         form = UserForm()

#     return render(request,"shop/main_page.html",{"new_user":form})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # перенаправляем на другую страницу
    else:
        form = ContactForm()
    return render(request, 'shop/main_page.html', {'form': form})


def tovar(request):
    if request.method == 'POST':
        form = TovarForm(request.POST)
        if form.is_valid():
            form.save()
        form = TovarForm()
    else:
        form = TovarForm()
        
    return render(request,'shop/tovar.html',{'form':form})
