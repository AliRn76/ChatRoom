from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout


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

