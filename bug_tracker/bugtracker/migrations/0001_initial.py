# Generated by Django 3.0.5 on 2020-12-05 19:15

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
            name='BugTicket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('dateTime', models.DateTimeField(auto_now_add=True)),
                ('type', models.CharField(choices=[('Development', 'Development'), ('Testing', 'Testing'), ('Production', 'Production')], max_length=30)),
                ('status', models.CharField(choices=[('Open', 'Open'), ('Resolved', 'Resolved'), ('Closed', 'Closed')], default='Open', max_length=30)),
                ('priority', models.CharField(choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')], default='Medium', max_length=30)),
                ('finderUserName', models.ForeignKey(db_constraint=False, on_delete=models.SET('Deleted User'), related_name='createdBy', to=settings.AUTH_USER_MODEL)),
                ('responsibleTeamMember', models.ForeignKey(db_constraint=False, on_delete=models.SET('Deleted User'), related_name='reponsibleUser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('dateTime', models.DateTimeField(auto_now_add=True)),
                ('bugTicket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='bugtracker.BugTicket')),
                ('user', models.ForeignKey(db_constraint=False, on_delete=models.SET('Deleted User'), to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
