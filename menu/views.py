from django.shortcuts import render
from django.contrib.auth.decorators import login_required 

@login_required

def menu_principal(request):
    return render(request, 'menu/menu_principal.html')

