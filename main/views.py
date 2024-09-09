from django.shortcuts import render

def show_main(request):
    context = {
        'name' : 'Gateron Linear Fizzy Oil ',
        'price': '8.000 / piece',
        'description': 'A linear profile keyboard switch with a smooth typing feel and loud clack'
    }

    return render(request, "main.html", context)

# Create your views here.
