from django.shortcuts import render

from account.models import Association, Address, CustomUser


def search_asso(request):
    """
    :param request: None
    :return: Return login page
    """
    return render(request, 'search_asso.html', locals())


def search_by_country(request):
    country = str(request.POST.get('search_country')).lower()
    country_db = Address.objects.filter(country=country).values('id')
    get_all_countries = []
    for c in country_db:
        get_all_countries.append(c['id'])
    association_user = []
    for a in get_all_countries:
        if CustomUser.objects.filter(address_id=a):
            association_user.append(CustomUser.objects.filter(
                address_id=a).values('association_id'))
    association = []
    for i in association_user:
        association.append(i[0])
    association_id = [v['association_id'] for v in association]
    association_search = []
    for j in association_id:
        association_search.append(Association.objects.filter(id=j).values())
    print(association_search)
    context = {
        'search_country': association_search,
    }
    return render(request, 'search_asso.html', context)


def search_by_city(request):
    pass
    """
    city = request.POST.get('search_city').lower()
    return render(request, 'search_asso.html', locals())"""


def search_by_name(request):
    pass
    """
    name = request.POST.get('search_name').lower()
    return render(request, 'search_asso.html', locals())"""
