from django.db import models
from enum import Enum 

class ProgressInfoEnum(Enum):
    INITIAL = "Initial"
    INPROGRESS = "In-progress"
    SUCCESS = "Success"
    FAILURE = "Failure"

class mailId_List(models.Model):
    email_id = models.EmailField()

class mail_History(models.Model):
    mail_subject = models.CharField(max_length=100)
    mail_content = models.TextField()
    progress = models.CharField(max_length=11 , choices=[(tag, tag.value) for tag in ProgressInfoEnum], default=ProgressInfoEnum.INITIAL)

