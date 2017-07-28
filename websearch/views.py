from django.shortcuts import render


# Create your views here.
def info_list(request):
    return render(request, 'websearch/info_list.html', {})
