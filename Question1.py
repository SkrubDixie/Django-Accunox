from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models

#Simple Class
class My_Model(models.Model):
    name = models.CharField()

# Defining signal receiver
@receiver(post_save, sender=My_Model)
def my_handler(sender, instance **kwargs):
    print('Saved Instance: ' + instance.name )

# Saving an instance

instance = My_Model(name='Test Instance')
instance.save()  # Triggering the post_save signal

# The my_handler function is connected to the post_save signal of
# the My_Model class which will be defined in models.py

# When instance.save() will be called, the signal is sent
# and my_handler is executed instantly with the output.

# this demonstrates trhat signal handler execute in the same time
# as signal sender, which shows synchronous behaviour.