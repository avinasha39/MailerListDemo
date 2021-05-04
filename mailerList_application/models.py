from django.db import models

class mailId_List(models.Model):
    email_id = models.EmailField()

class mail_History(models.Model):
    mail_subject = models.CharField()
    mail_content = models.TextField()
    progress = models.CharField() #enum 

'''
enum : initial(default), in-progress, sucess, failure
event based programming -> 

'''

