from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User


from .forms import LoginForm, ParagraphErrorList, MemberForm, AssociationForm
from .models import CustomUser, Association, Address


@csrf_exempt
def login_view(request):
    """
    :param request: None
    :return: Return login page
    """
    error = False
    form = LoginForm(request.POST or None, error_class=ParagraphErrorList)
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(request, username=username, password=password)
        print(user)
        user_chosen = User.objects.filter(username=username)
        user_type = CustomUser.objects.filter(user=user_chosen)
        if user is not None and user_type.user_type == 'AS':
            login(request, user)
            print("good")
            return render(request,
                          'association/welcome_association.html',
                          locals())
        elif user is not None and user_type == 'ME':
            print("pas good")
            login(request, user)
            return render(request, 'home/home.html',
                          locals())
        else:
            print('pas good good')
            error = True
            return render(request, 'login/login.html', locals())
    else:
        return render(request, 'login/login.html', locals())


def logout_view(request):
    """
    :param request: Click the button logout
    :return: homepage
    """
    logout(request)
    return render(request, 'home/accueil.html', locals())


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
        print(form.cleaned_data)
        name = form.cleaned_data['name']
        street = form.cleaned_data['street']
        zip_code = form.cleaned_data['zip_code']
        city = form.cleaned_data['city']
        country = form.cleaned_data['country']
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        re_email = form.cleaned_data['re_email']
        re_password = form.cleaned_data['re_password']
        user = User(username=email,  email=email, password=password,
                    last_name=last_name, first_name=first_name)
        address = Address(street=street, zip_code=zip_code, city=city,
                          country=country)
        association = Association(name=name)
        # AS Like Association
        user_type = 'AS'
        custom_user = CustomUser(user=user, address_id=address,
                                 association_id=association,
                                 user_type=user_type)
        user.save()
        address.save()
        association.save()
        custom_user.save()
        form = LoginForm()
        return render(request, 'login/login.html', {'form': form})
    else:
        return render(request, 'login/registration_association.html', locals())


def welcome_association(request):
    return render(request, 'association/welcome_association.html', locals())
