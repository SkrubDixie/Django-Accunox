import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hello.settings")

import django
django.setup()

from django.core.management import call_command

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Model1(models.Model):
    name = models.CharField()

@receiver(post_save, sender=Model1)
def handler1(sender, instance, **kwargs):
    print("Instance: "+ instance)

instance = Model1(name='Test')
instance.save