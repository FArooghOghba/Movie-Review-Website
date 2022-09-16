from django.shortcuts import render


def error_404_view(request, exception):
    # we add the path to the the 404.html file
    # here. The name of our HTML file is 404.html
    return render(request, template_name='page_404.html')
