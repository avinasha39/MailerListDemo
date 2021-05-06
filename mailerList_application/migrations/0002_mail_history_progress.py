# Generated by Django 3.2.1 on 2021-05-06 19:28

from django.db import migrations, models
import mailerList_application.models


class Migration(migrations.Migration):

    dependencies = [
        ('mailerList_application', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mail_history',
            name='progress',
            field=models.CharField(choices=[(mailerList_application.models.ProgressInfoEnum['INITIAL'], 'Initial'), (mailerList_application.models.ProgressInfoEnum['INPROGRESS'], 'In-progress'), (mailerList_application.models.ProgressInfoEnum['SUCCESS'], 'Success'), (mailerList_application.models.ProgressInfoEnum['FAILURE'], 'Failure')], default=mailerList_application.models.ProgressInfoEnum['INITIAL'], max_length=11),
        ),
    ]
