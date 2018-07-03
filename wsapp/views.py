from django.shortcuts import render

# Create your views here.


# place holder views

def static_view(request):
    return render(request, 'static.html')


def react_enabled_view(request):
    return render(request, 'reactEnabled.html')


def js_enabled_view(request):
    return render(request, 'jsEnabled.html')