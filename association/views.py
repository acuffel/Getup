from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
import stripe
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
    print(association_filter)
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
    save = False
    if form.is_valid():
        email = form.cleaned_data['email']
        first_name = form.cleaned_data['first_name'].lower()
        last_name = form.cleaned_data['last_name'].lower()
        amount = form.cleaned_data['amount']
        create_payment(amount)
        donor = Donor.objects.create(email=email, first_name=first_name,
                                          last_name=last_name)
        donor.save()
        form = DonorForm()
        save = True
        context = {
            'association': association,
            'form': form,
            'save': save,
        }
        return render(request, 'make_donation.html', context)
    else:
        form = DonorForm()
        context = {
            'association': association,
            'form': form,
        }
        return render(request, 'make_donation.html', context)


def create_payment(amount):
    try:
        intent = stripe.PaymentIntent.create(
            amount=amount,
            currency='eur',
        )
        return JsonResponse({
          'clientSecret': intent['client_secret']
        })
    except Exception as e:
        return JsonResponse({'error': str(e)})
