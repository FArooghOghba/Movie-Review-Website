from django.shortcuts import render


# Create your views here.

def index_view(request):
    return render(request, template_name='website/index.html')


def blog_list_view(request):
    return render(request, template_name='website/blog_list.html')


def about_view(request):
    return render(request, template_name='website/about.html')


def contact_view(request):
    return render(request, template_name='website/contact.html')
