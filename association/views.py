from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from account.models import Association, Address, CustomUser
from .forms import DonorForm
from .models import Donor, Donation


def search_asso(request):
    """
    :param request: None
    :return: Return login page
    """
    return render(request, 'search_asso.html', locals())


def search_by_country(request):
    country = str(request.POST.get('search_country')).lower()
    country_db = Address.objects.filter(country=country).values('id')
    user_id = CustomUser.objects.filter(address_id__in=country_db).values('association_id')
    association_filter = Association.objects.filter(id__in=user_id).values()
    context = {
        'search': association_filter,
    }
    return render(request, 'search_asso.html', context)


def search_by_city(request):
    city = str(request.POST.get('search_city')).lower()
    country_db = Address.objects.filter(city=city).values('id')
    user_id = CustomUser.objects.filter(address_id__in=country_db).values(
        'association_id')
    association_filter = Association.objects.filter(id__in=user_id).values()
    context = {
        'search': association_filter,
    }
    return render(request, 'search_asso.html', context)


def search_by_name(request):
    name_filter = str(request.POST.get('search_name')).lower()
    association_filter = Association.objects.filter(
        name__contains=name_filter).values()
    context = {
        'search': association_filter,
    }
    return render(request, 'search_asso.html', context)


def home_asso(request, association_id):
    association = Association.objects.filter(id=association_id).values()
    context = {
        'association': association,
    }
    return render(request, 'home_asso.html', context)


@csrf_exempt
def make_donation(request, association_id):
    association = Association.objects.filter(id=association_id).values()
    form = DonorForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data['email']
        first_name = form.cleaned_data['first_name'].lower()
        last_name = form.cleaned_data['last_name'].lower()
        amount = form.cleaned_data['amount']
        donor = Donor.objects.create(email=email, first_name=first_name,
                                          last_name=last_name)
        donor.save()
        context = {
            'association': association,
            'amount': amount,
            'name': first_name,
            'email': email,
        }
        return render(request, 'payment.html', context)
    else:
        form = DonorForm()
        context = {
            'association': association,
            'form': form,
        }
        return render(request, 'make_donation.html', context)


def validate_donation(request, email, association_id, amount):
    donor = Donor.objects.get(email=email)
    asso = Association.objects.get(id=association_id)
    donation = Donation.objects.create(amount=amount, donor_id=donor,
                                       association_id=asso)
    donation.save()
    association = Association.objects.filter(id=association_id).values()
    context = {
        'email': email,
        'association': association,
        'amount': amount,
    }
    return render(request, 'validate_donation.html', context)
