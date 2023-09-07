from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Fernanda Nadhiftya Putra',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)
