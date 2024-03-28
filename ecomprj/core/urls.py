from django.urls import path
from core.views import index, contact, about_us, purchase_guide, privacy_policy, terms_of_service,sell

app_name = "core"

urlpatterns = [

    # Homepage
    path("", index, name="index"),
    path("contact/", contact, name="contact"),

    path("about_us/", about_us, name="about_us"),
    path("purchase_guide/", purchase_guide, name="purchase_guide"),
    path("privacy_policy/", privacy_policy, name="privacy_policy"),
    path("terms_of_service/", terms_of_service, name="terms_of_service"),
    path("sell/", sell, name="sell"),
]