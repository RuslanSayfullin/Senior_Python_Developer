from django.db import models


class Client(models.Model):
    phone_number = models.CharField(max_length=11)
    operator_code = models.CharField(max_length=3)
    tag = models.CharField(max_length=255)
    timezone = models.CharField(max_length=255)


class MailingList(models.Model):
    start_time = models.DateTimeField()
    message = models.TextField()
    filter_operator_code = models.CharField(max_length=3)
    filter_tag = models.CharField(max_length=255)
    end_time = models.DateTimeField()


class Message(models.Model):
    created_time = models.DateTimeField()
    status = models.CharField(max_length=255)
    campaign = models.ForeignKey(MailingList, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)