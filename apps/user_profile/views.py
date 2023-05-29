from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate,logout
from .forms import *
from .models import * 
from apps.user_profile.models import CustomUser as User

# Create your views here.


def change_password(request):
    # import ipdb;ipdb.set_trace()
    user = request.user
    model = "old"

    if request.POST:
       # Handle post request
       old = request.POST["old_password"]
       new = request.POST['new_password']
       conf = request.POST['confirm_password']

       e1 = '' if new else "Password can't be left blank"
       e3 = '' if old else "Password can't be left blank"
       e2 = '' if conf else "Password can't be left blank"

       if request.user != authenticate(username=request.user.username, password=old):
           e3 = " Incorrect password"
       elif len(new) < 6 and new:
           e1 = "Password should be atleast 6 charactors"
       elif conf != new:
           e2 = "Passwords doesn't match, please try again."

       elif not any([e1, e2, e3]):
           user.set_password(new)
           user.save()
           return HttpResponseRedirect(
               "/login/"
           )
    # Render to template
    return render(request, 'registration/change_password.html', locals())

@login_required
def user_profile(request):
    context = {}
    try:
        user_data= User.objects.get(id=request.user.id)
        context['user'] = user_data
    except User.DoesNotExist:
        user =None
    return  render(request,'user_profile.html',locals())


@login_required
def edit_user_profile(request):
    usr = User.objects.get(id=request.user.id)    
    print(request.POST)
    if request.method== "POST":
        form = UserProfileEditForm(request.POST,request.FILES)
        form.actual_user = request.user
        if form.is_valid():
            email = request.POST.get('email')
            check = User.objects.filter(email=email).exclude(id=request.user.id).exists()
            if not check:
                print("I am here")
                usr.first_name = request.POST.get('first_name')               
                usr.email = email
                usr.save()
                
                birth_date = request.POST.get('birth_date')
                if birth_date != '':
                    usr.birth_date = birth_date
                
                contact = request.POST.get('contact')
                if contact != '':
                    usr.contact = contact
                     
                secondary_email = request.POST.get('secondary_email')
                usr.secondary_email = secondary_email

                gender = request.POST.get('gender')
                if gender != '':
                    usr.gender = gender
                
                try:
                    usr.profile_pic = request.FILES['profile_pic']
                except MultiValueDictKeyError:
                    pass

                usr.save()
                return redirect('profile')
                
            else:
                form = UserProfileEditForm(request.POST)
                error = "Email already exists in our database"
        else:
            form = UserProfileEditForm(request.POST)
    else:
        form = UserProfileEditForm(initial={
            'first_name':usr.first_name,
            'email':usr.email,
            'contact':usr.contact,
            'last_name':usr.last_name,
            'profile_pic':usr.profile_pic.url,
          })
    return render(request,'edit_user_profile.html', locals())