
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView

from chat.views import logout_view

urlpatterns = [
    path('', include("chat.urls")),
    path('admin/', admin.site.urls),
    path('logout/', logout_view, name="logout"),
    path('d_login/', LoginView.as_view(template_name='desktop_login.html'), name="desktop_login"),
    path('m_login/', LoginView.as_view(template_name='mobile_login.html'), name="mobile_login"),

]
