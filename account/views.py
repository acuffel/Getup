from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User


from .forms import LoginForm, ParagraphErrorList, MemberForm, AssociationForm, \
    UploadAssociation
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
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(request, username=username, password=password)
        user_chosen = User.objects.filter(username=username).values('id')
        user_id = [v['id'] for v in user_chosen]
        custom_chosen = CustomUser.objects.filter(
            user=user_id[0]).values('user_type')
        user_type = [v['user_type'] for v in custom_chosen]
        if user is not None and user_type == ['AS']:
            login(request, user)
            return render(request,
                          'association/welcome_association.html',
                          locals())
        elif user is not None and user_type == ['ME']:
            login(request, user)
            return render(request, 'home/home.html',
                          locals())
        else:
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
    return render(request, 'home/homepage.html', locals())


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
        name = form.cleaned_data['name'].lower()
        street = form.cleaned_data['street'].lower()
        zip_code = form.cleaned_data['zip_code']
        city = form.cleaned_data['city'].lower()
        country = form.cleaned_data['country'].lower()
        first_name = form.cleaned_data['first_name'].lower()
        last_name = form.cleaned_data['last_name'].lower()
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        re_email = form.cleaned_data['re_email']
        re_password = form.cleaned_data['re_password']
        user = User.objects.create_user(username=email,  email=email, password=password,
                    last_name=last_name, first_name=first_name)
        address = Address.objects.create(street=street, zip_code=zip_code, city=city,
                          country=country)
        association = Association.objects.create(name=name)
        # AS Like Association
        user_type = 'AS'
        custom_user = CustomUser.objects.create(user=user, address=address,
                                 association=association,
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


def show_information(request):
    """
    :param:
    :return:
    """
    user_id = request.user.id
    user_asso = User.objects.filter(pk=user_id)
    info_asso = CustomUser.objects.filter(user_id=user_id).values()
    address_id = [v['address_id'] for v in info_asso]
    address_asso = Address.objects.filter(id=address_id[0])
    context = {
        'address_asso': address_asso,
        'user_asso': user_asso,
    }
    return render(request, 'association/info_association.html', context)


def show_association(request):
    """
    :param:
    :return:
    """
    user_id = request.user.id
    info_asso = CustomUser.objects.filter(user_id=user_id).values('association_id')
    asso_id = [v['association_id'] for v in info_asso]
    my_association = Association.objects.filter(id=asso_id[0])
    context = {
        'my_association': my_association,
    }
    return render(request, 'association/my_association.html', context)


@csrf_exempt
def asso_upload_view(request):
    """Process images uploaded by users"""
    user_id = request.user.id
    info_asso = CustomUser.objects.filter(user_id=user_id).values(
        'association_id')
    asso_id = [v['association_id'] for v in info_asso]
    my_association = Association.objects.filter(id=asso_id[0])
    form = UploadAssociation(request.POST or None, request.FILES or None)
    if form.is_valid():
        print("form valid")
        update_asso = Association.objects.get(id=asso_id[0])
        update_asso.picture = form.cleaned_data["picture"]
        update_asso.description = form.cleaned_data["description"]
        update_asso.category = form.cleaned_data["category"]
        update_asso.save()
        return render(request,
                      'association/welcome_association.html', locals())
    else:
        context = {
            'form': form,
            'association': my_association,
        }
        print("form not valid")
    return render(request, 'association/update_association.html', context)
