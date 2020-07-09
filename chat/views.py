from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.utils.datetime_safe import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout

from chat.forms import SingupForm


def my_view(request):

    # Let's assume that the visitor uses an iPhone...
    print(request.user_agent.is_mobile) # returns True
    print(request.user_agent.is_tablet) # returns False
    print(request.user_agent.is_touch_capable) # returns True
    print(request.user_agent.is_pc )# returns False
    print(request.user_agent.is_bot ) #returns False

    # Accessing user agent's browser attributes
    print(request.user_agent.browser ) # returns Browser(family=u'Mobile Safari', version=(5, 1), version_string='5.1')
    print(request.user_agent.browser.family  )# returns 'Mobile Safari'
    print(request.user_agent.browser.version  )# returns (5, 1)
    print(request.user_agent.browser.version_string )  # returns '5.1'

    # Operating System properties
    print(request.user_agent.os ) # returns OperatingSystem(family=u'iOS', version=(5, 1), version_string='5.1')
    print(request.user_agent.os.family)  # returns 'iOS'
    print(request.user_agent.os.version  )# returns (5, 1)
    print(request.user_agent.os.version_string  )# returns '5.1'

    # Device properties
    print(request.user_agent.device ) # returns Device(family='iPhone')
    print(request.user_agent.device.family)  # returns 'iPhone'
    return HttpResponse("User is mobile: <b>"           + str(request.user_agent.is_mobile)             + "</b><br><br>" +
                        "User is tablet: <b>"           + str(request.user_agent.is_tablet)             + "</b><br><br>" +
                        "User is touch capable: <b>"    + str(request.user_agent.is_touch_capable)      + "</b><br><br>" +
                        "User is pc: <b>"               + str(request.user_agent.is_pc)                 + "</b><br><br>" +
                        "User is bot: <b>"              + str(request.user_agent.is_bot)                + "</b><br><br>" +
                        "User browser: <b>"             + str(request.user_agent.browser)               + "</b><br><br>" +
                        "User borwser family: <b>"      + str(request.user_agent.browser.family)        + "</b><br><br>" +
                        "User browser version: <b>"     + str(request.user_agent.browser.version_string)+ "</b><br><br>" +
                        "User os: <b>"                  + str(request.user_agent.os.family)             + "</b><br><br>" +
                        "User os version: <b>"          + str(request.user_agent.os.version_string)     + "</b><br><br>")


def main_view(request):
    try:
        print("Welcome " + request.user.username)
        # If taraf First_name nadasht --> Login nashode
        context = {
            "name": request.user.first_name,
        }

    except:
        if request.user_agent.is_pc:
            form = SingupForm(request.POST or None)
            if request.method == "POST":
                user = User
                print("* YE CHIZI POST SHOD")
                if form.is_valid():
                    print("* FORM WAS VALID")
                    user.first_name = form.cleaned_data.get("first_name")
                    user.last_name = form.cleaned_data.get("last_name")
                    user.username = form.cleaned_data.get("username")
                    user.password = form.cleaned_data.get("password")
                    user.objects.create_user(user.username, "", user.password, first_name=user.first_name,
                                             last_name=user.last_name, is_staff=True)
                    print("* User Create Successfully")
                else:
                    print("* FORM WAS INVALID")
                    print(form.errors)
            context = {
                "form": form
            }
            return render(request, "desktop_login.html", context)
        else:
            print("It's Mobile & Tablet Login")
            return render(request, "mobile_login.html", {})
            # return HttpResponse("It's Mobile & Tablet Login")
        # return render(request, "login.html", {})

    # return render(request, "main.html", context)
    return HttpResponse("Hello " + request.user.username)


def logout_view(request):
    print("Bye " + request.user.username)
    # with open('log.txt', 'a') as file:
    #     data = str(datetime.now()) + " Bye " + request.user.username + "\n"
    #     file.write(data)

    logout(request)
    return redirect("/")

def singup_view(request):
    pass
    # user = User
    # if request.method == "POST":
    #     form = SingupForm(request.POST)
    #     if form.is_valid():
    #         user.first_name = form.cleaned_data.get("name")
    #         user.last_name  = form.cleaned_data.get("lastname")
    #         user.username   = form.cleaned_data.get("username")
    #         user.password   = form.cleaned_data.get("password")
    #         user.objects.create_user(user.username, "", user.password, first_name=user.first_name, last_name=user.last_name, is_staff=True)
    #
    #         return redirect("../login")
    # else:
    #     form = SingupForm()
    #
    # context = {
    #     "form" : form
    # }
    # return render(request, "signup.html", context)

