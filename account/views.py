from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt

from .forms import LoginForm, ParagraphErrorList, MemberForm
from .models import Member


@csrf_exempt
def login(request):
    """
    :param request: None
    :return: Return login page
    """
    error = False
    form = LoginForm(request.POST or None, error_class=ParagraphErrorList)
    if form.is_valid():
        email = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'account/account.html', locals())
        else:
            error = True
            return render(request, 'login/login.html', locals())
    else:
        return render(request, 'login/login.html', locals())


@csrf_exempt
def registration(request):
    """
    :param request: None
    :return: Connexion page is the form is valid
    """
    form = MemberForm(request.POST or None, error_class=ParagraphErrorList)
    if form.is_valid():
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        """
        member = Member.objects.create(username, email, password)
        Member.save()
        form = LoginForm(None)
        """
        envoi = True
        return render(request, 'login/registration.html', locals())
    else:
        return render(request, 'login/registration.html', locals())
