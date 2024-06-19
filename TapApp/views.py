from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import User

def hello(request):
    return HttpResponse("Hello, world!")

def users_list(request):
    users = User.objects.all()
    return render(request, 'users_list.html', {'users': users})

def new_user(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        age = request.POST['age']
        User.objects.create(name=name, email=email, age=age)
        return redirect('users_list')
    return render(request, 'new_user.html')



def edit_user(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        user.name = request.POST['name']
        user.email = request.POST['email']
        user.age = request.POST['age']
        user.save()  
        return redirect('users_list')  
    return render(request, 'edit_user.html', {'user': user})


def delete_user(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        user.delete()
        return redirect('users_list')
    return render(request, 'delete_user.html', {'user': user})
