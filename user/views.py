from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def Login(request):
    if request.method == 'POST':

        # AuthenticationForm_can_also_be_used__

        email = request.POST.get('email')
        print(email)
        password = request.POST.get('password')
        print(password)
        user = NewUser.objects.filter(email=email).first()
        if user:
            if user.is_active == False:
                messages.error(request, "Account not verified")
            else:
                user = authenticate(request, email=email, password=password)

                if user is not None:
                    login(request, user)
                    return redirect(request.GET.get('next', 'home'))
                else:
                    print("errrr")
                    messages.error(
                        request, 'Password is incorrect for the email address entered ')
        else:
            print("email not registered")
            messages.error(request, 'Email is not registered')

    return render(request, 'authentication/login.html')    
