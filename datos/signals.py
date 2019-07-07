from datos.models import DatosModel

from django.db.models.signals import post_save
from django.dispatch import receiver
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


@receiver(post_save, sender=DatosModel)
def announce_new_user(sender, instance, created, **kwargs):
    if created:
        print("se llamo al signal de data")
        channel_layer = get_channel_layer()
        print("channel layer de datos:",channel_layer)
        async_to_sync(channel_layer.group_send)(
            "gossip2", {"type": "data.new",
                       "event": "New Data",
                       "nombre": instance.nombre})
