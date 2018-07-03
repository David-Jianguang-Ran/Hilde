from django.shortcuts import render

# Create your views here.


# place holder views
def static_view(request):
    return render(request, 'title.html')


def live_view(request):
    return render(request, 'main.html')