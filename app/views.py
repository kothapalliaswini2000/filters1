from django.shortcuts import render

# Create your views here.
import datetime
def filters(request):
    da=datetime.datetime.now()
    d={'data':'THis iS My wOrLd','d': da,'c':5}
    return render(request,'filters.html',d)


def userfilters(request):
    d={'data':'hi PYthOn WhErE ArE yOu'}
    return render(request,'userfilters.html',d)
