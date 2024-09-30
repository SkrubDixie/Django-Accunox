import threading
from django.core.signals import request_finished
from django.dispatch import receiver

# Signal receiver function to show the current thread
@receiver(request_finished)
def show_current_thread(sender, **kwargs):
    current_thread = threading.current_thread()
    print('Signal received in thread: ' + current_thread.name) # Prints the name of the thread that calls it

# Sending a signal in the main thread
print('Signal sent in thread: ' + threading.current_thread().name) # Prints the thread name before sending signal

request_finished.send(sender=None)
# When this is run, it will also print the same thread name
# This demonstrates that signals run in the same thread as the caller.

