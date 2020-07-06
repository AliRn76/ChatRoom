from django.db import models
from django.conf import settings


User = settings.AUTH_USER_MODEL


class Room(models.Model):
    id          = models.AutoField(db_column='ID', primary_key=True)
    roomname    = models.CharField(db_column='RoomName', max_length=64, blank=True, null=True)
    membercount = models.IntegerField(db_column='MemberCount', blank=True, null=True)
    pv          = models.BooleanField(db_column='Pv', default=False)
    unreadcount = models.IntegerField(db_column='UnreadCount', default=0)

    class Meta:
        db_table = 'Room'

    def __str__(self):
        return "RoomID: " + str(self.id)




class Chat(models.Model):
    id          = models.AutoField(db_column='ID', primary_key=True)
    userid      = models.ForeignKey(User, models.DO_NOTHING, db_column='UserID', null=True)
    message     = models.TextField(db_column='Message', blank=True, null=True)
    roomid      = models.ForeignKey(Room, models.DO_NOTHING, db_column='RoomID', blank=True, null=True)
    datetime    = models.DateTimeField(db_column='Datetime', blank=True)
    unread      = models.BooleanField(db_column='Unread', default=False)
    image       = models.ImageField(db_column='Image', upload_to='images/', blank=True, null=True)

    class Meta:
        db_table = 'Chat'

    def __str__(self):
        return str(self.userid.username) + "     : " + str(self.message) + "     roomid: " + str(self.roomid_id) + "     unread: " + str(self.unread)



class Member(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    userid = models.ForeignKey(User, models.DO_NOTHING, db_column='UserID', blank=True, null=True)
    roomid = models.ForeignKey(Room, models.DO_NOTHING, db_column='RoomID', blank=True, null=True)

    class Meta:
        db_table = 'Member'

    def __str__(self):
        return str(self.userid) + "        roomid: " + str(self.roomid)


