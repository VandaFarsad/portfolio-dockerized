from django.urls import path

from .views import ImpressumView, IndexView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("impressum/", ImpressumView.as_view(), name="impressum"),
]
