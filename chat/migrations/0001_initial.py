# Generated by Django 3.0.8 on 2020-07-06 23:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('roomname', models.CharField(blank=True, db_column='RoomName', max_length=64, null=True)),
                ('membercount', models.IntegerField(blank=True, db_column='MemberCount', null=True)),
                ('pv', models.BooleanField(db_column='Pv', default=False)),
                ('unreadcount', models.IntegerField(db_column='UnreadCount', default=0)),
            ],
            options={
                'db_table': 'Room',
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('roomid', models.ForeignKey(blank=True, db_column='RoomID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='chat.Room')),
                ('userid', models.ForeignKey(blank=True, db_column='UserID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Member',
            },
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('message', models.TextField(blank=True, db_column='Message', null=True)),
                ('datetime', models.DateTimeField(blank=True, db_column='Datetime')),
                ('unread', models.BooleanField(db_column='Unread', default=False)),
                ('image', models.ImageField(blank=True, db_column='Image', null=True, upload_to='images/')),
                ('roomid', models.ForeignKey(blank=True, db_column='RoomID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='chat.Room')),
                ('userid', models.ForeignKey(db_column='UserID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Chat',
            },
        ),
    ]
