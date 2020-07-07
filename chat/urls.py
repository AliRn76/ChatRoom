from django.urls import path, include

from chat.views import *


urlpatterns = [
    # path('api/', include('chat.api.urls')),

    # path('<int:room_id>/<int:msg_id>/delete', chat_delete_view, name="chat_delete"),
    path('detect', my_view),
    path('', main_view)
]