from django.shortcuts import render
from django.utils import timezone
from .models import Info

# Create your views here.
def info_list(request):
    infos = Info.objects.all().order_by('-year').order_by('-created_date')
    return render(request, 'websearch/info_list.html', {'infos': infos})
