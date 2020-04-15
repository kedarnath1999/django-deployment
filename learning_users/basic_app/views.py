from django.shortcuts import render
from basic_app.forms import UserForm,UserProfileInfoForm


from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse  ## to get back to the samepage
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'basic_app/index.html')

@login_required  ## this a special page which will work only if u are logged in
def special(request):
    return HttpResponse("You are logged in nice!")

@login_required
def user_logout(request):
    print(request)
    logout(request)  ### u dont need to know which user u just have to logout unlike login
    return HttpResponseRedirect(reverse('index'))

def register(request):

    registered = False  ## will be set to true if registered

    if request.method == "POST":
        user_form = UserForm(data =request.POST)  ## we get information from the form
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()   ## here we save all the contents in the form  given by the user
            user.set_password(user.password)   ## here we using hashing to hash the password provoded by the user
            ## user.set_password -> this method id used to encrypt the data
            ##  user.password is the data
            user.save()


            # to avoid collission we do not commit
            profile  = profile_form.save(commit=False)
            profile.user = user
            ## 'user' in model.py which we have created and the user in 'user = user_form.save()' is same

            if  'profile_pic' in request.FILES: ##if the user has sent files
                profile.profile_pic = request.FILES['profile_pic'] #this is a dictionary, profile_pic in forms.pys
                 # stores it into profile_pic present in models.py
            profile.save()  ## will commit

            registered=True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request,'basic_app/registration.html',{'user_form':user_form,
                                                            'profile_form':profile_form,
                                                            'registered':registered})

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')  ## cos we have given name='username' in login.html page
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)
        ## user -> will contain just the username
        ## will check username and password_validation
        print(user)

        if user:
            if user.is_active:
                login(request,user)  ## built-in function  ##u need to know whih user
                return HttpResponseRedirect(reverse('index'))  ## will redirect back to index page
                # if we do not use 'reverse' then it will search or url 'basic_app/user_login/index' and not 'index'

            else:
                return HttpResponse("Account has been deactivated")

        else:
            print("someone tried to login and failed!")
            print("Username: {} and password {}".format(username,password))
            return HttpResponse("Invalid login details supplied")

    else:
        return render(request,'basic_app/login.html',{})
