from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from notifier.consumers import NoseyConsumer
from datos.consumer import DataConsumer
application = ProtocolTypeRouter({
    "websocket": URLRouter([
        path("notifications/", NoseyConsumer),
        path("data/", DataConsumer)
    ])
})
