from django.shortcuts import render


def homepage(request):
    """
    :param request: None
    :return: HomePage
    """
    return render(request, 'home/homepage.html', locals())

