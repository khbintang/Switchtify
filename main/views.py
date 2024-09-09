from django.shortcuts import render

def show_main(request):
    context = {
        'name' : 'Gateron Linear Fizzy Oil Keyboard Switch ',
        'price': 'Rp 8.000 / piece',
        'type' : ' Linear',
        'sound_profile' : 'Loud clacky, almost marbly',
        'lube': 'Factory lubed'
    }

    return render(request, "main.html", context)

# Create your views here.
