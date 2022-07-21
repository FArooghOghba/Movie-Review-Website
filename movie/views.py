from django.shortcuts import render


# Create your views here.

def movie_list_view(request):
    return render(request, template_name='website/movie_list.html')
