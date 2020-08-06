from django.shortcuts import render


def about(request):
    """
    :param request: None
    :return: About Page
    """
    return render(request, 'about/about.html', locals())
