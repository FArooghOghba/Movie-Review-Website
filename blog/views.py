from django.shortcuts import render


# Create your views here.

def blog_list_view(request):
    return render(request, template_name='blog/blog_list.html')


def blog_single_view(request):
    return render(request, template_name='blog/blog_single.html')
