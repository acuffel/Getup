from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt

from .forms import LoginForm, ParagraphErrorList, MemberForm, AssociationForm


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
def member_registration(request):
    """
    :param request: None
    :return: Connexion page is the form is valid
    """
    form = MemberForm(request.POST or None, error_class=ParagraphErrorList)
    if form.is_valid():
        civility = form.cleaned_data['civility']
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        birth_date = form.cleaned_data['birth_date']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        """
        member = Member.objects.create(username, email, password)
        Member.save()
        form = LoginForm(None)
        """
    context = {
        'form': form
    }
    return render(request, 'login/registration_member.html', context)


@csrf_exempt
def association_registration(request):
    form = AssociationForm(request.POST or None, error_class=ParagraphErrorList)
    if form.is_valid():
        name = form.cleaned_data['name']
        address = form.cleaned_data['address']
        post_code = form.cleaned_data['post_code']
        city = form.cleaned_data['city']
        country = form.cleaned_data['country']
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        birth_date = form.cleaned_data['birth_date']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        """
        member = Member.objects.create(username, email, password)
        Member.save()
        form = LoginForm(None)
        """
    context = {
        'form': form
    }
    return render(request, 'login/registration_association.html', context)
