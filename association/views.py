from django.shortcuts import render

from account.models import Association, Address, CustomUser
from django.contrib.postgres.search import SearchQuery


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
