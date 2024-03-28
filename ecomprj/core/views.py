from django.shortcuts import render

def index(request):
    return render(request, "core/index.html")

# Other Pages 
def contact(request):
    return render(request, "core/contact.html")

def about_us(request):
    return render(request, "core/about_us.html")


def purchase_guide(request):
    return render(request, "core/purchase_guide.html")

def privacy_policy(request):
    return render(request, "core/privacy_policy.html")

def terms_of_service(request):
    return render(request, "core/terms_of_service.html")

def sell(request):
    return render(request, "core/sell.html")


