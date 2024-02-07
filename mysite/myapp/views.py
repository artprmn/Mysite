# myapp/views.py
from .models import UserProfile, Campaign, House
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm, UserProfileForm
from .forms import CampaignForm
from django.shortcuts import  get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import House, ApartmentVisit
from .forms import ApartmentVisitForm
from .forms import HouseForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Count


@login_required
def delete_house(request, house_id):
    house = get_object_or_404(House, pk=house_id)
    house.delete()
    return HttpResponseRedirect(reverse('campaign_detail', kwargs={'campaign_id': house.campaign.id}))


@login_required
def delete_campaign(request, campaign_id):
    campaign = get_object_or_404(Campaign, pk=campaign_id)
    campaign.delete()
    return HttpResponseRedirect(reverse('user_profile'))



def enter_apartment_visit(request, house_id):
    house = House.objects.get(pk=house_id)

    if request.method == 'POST':
        form = ApartmentVisitForm(request.POST)
        if form.is_valid():
            apartment_visit = form.save(commit=False)
            apartment_visit.user = request.user
            apartment_visit.house = house
            apartment_visit.save()
            return redirect('house_detail', house_id=house_id)
    else:
        form = ApartmentVisitForm()

    return render(request, 'enter_apartment_visit.html', {'form': form, 'house': house})
def house_detail(request, house_id):
    house = House.objects.get(pk=house_id)
    visits = ApartmentVisit.objects.filter(house=house)
    return render(request, 'house_detail.html', {'house': house, 'visits': visits})

def apartment_visit(request, house_id):
    house = get_object_or_404(House, pk=house_id)
    user = request.user

    if request.method == 'POST':
        form = ApartmentVisitForm(request.POST)
        if form.is_valid():
            visit = form.save(commit=False)
            visit.house = house
            visit.user = user
            visit.save()
            return redirect('house_detail', house_id=house.id)
    else:
        form = ApartmentVisitForm()

    return render(request, 'myapp/apartment_visit.html', {'form': form, 'house': house})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            print("Login successful. Redirecting to user_profile.")
            return redirect('user_profile')
        else:
            print("Form is not valid. Errors:", form.errors)
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            user = authenticate(request, username=user_form.cleaned_data['username'], password=user_form.cleaned_data['password1'])
            login(request, user)
            print("Registration successful. Redirecting to user_profile.")
            return redirect('user_profile')
        else:
            print("Form(s) is not valid. Errors - User Form:", user_form.errors, "Profile Form:", profile_form.errors)
    else:
        user_form = RegistrationForm()
        profile_form = UserProfileForm()
    return render(request, 'registration/register.html', {'user_form': user_form, 'profile_form': profile_form})

# myapp/views.py
@login_required
def user_profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    campaigns = Campaign.objects.filter(owner=user_profile.user)
    houses = House.objects.filter(campaign__in=campaigns)# Измененная строка
    return render(request, 'user_profile.html', {'user_profile': user_profile, 'campaigns': campaigns})



@login_required
def create_house(request, campaign_id):
    campaign = Campaign.objects.get(pk=campaign_id)
    if request.method == 'POST':
        form = HouseForm(request.POST)
        if form.is_valid():
            house = form.save()
            campaign.houses.add(house)
            return redirect('user_profile')
    else:
        form = HouseForm()
    return render(request, 'create_house.html', {'form': form})

@login_required
def edit_profile(request):
    user_profile = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('user_profile')
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'edit_profile.html', {'form': form})


def home(request):
    # Логика для титульной страницы
    return render(request, 'home.html')


def user_page(request, username):
    # Логика для страницы пользователя
    return render(request, 'user_page.html')


def user_logout(request):
    logout(request)
    return redirect('home')


@login_required
def create_campaign(request):
    if request.method == 'POST':
        form = CampaignForm(request.POST)
        if form.is_valid():
            campaign = form.save(commit=False)
            campaign.owner = request.user  # Присваиваем текущего пользователя, а не UserProfile
            campaign.save()
            return redirect('user_profile')
    else:
        form = CampaignForm()
    return render(request, 'create_campaign.html', {'form': form})

def campaign_detail(request, campaign_id):
    campaign = get_object_or_404(Campaign, pk=campaign_id)
    houses = campaign.houses.all()

    return render(request, 'campaign_detail.html', {'campaign': campaign, 'houses': houses})

@login_required
def add_house(request, campaign_id):
    campaign = get_object_or_404(Campaign, pk=campaign_id)

    if request.method == 'POST':
        form = HouseForm(request.POST)
        if form.is_valid():
            house = form.save(commit=False)
            house.campaign = campaign
            house.save()
            return redirect('campaign_detail', campaign_id=campaign_id)
    else:
        form = HouseForm()

    return render(request, 'add_house.html', {'form': form, 'campaign': campaign})


from django.shortcuts import render
from django.db.models import Count
from .models import Campaign, House, ApartmentVisit


from django.db.models import Count

def campaign_statistics(request):
    campaigns = Campaign.objects.all()
    campaign_data = []

    for campaign in campaigns:
        total_visits = campaign.houses.aggregate(total=Count('apartmentvisit'))['total']
        positive_reactions = ApartmentVisit.objects.filter(house__campaign=campaign, reaction='positive').count()
        neutral_reactions = ApartmentVisit.objects.filter(house__campaign=campaign, reaction='neutral').count()
        negative_reactions = ApartmentVisit.objects.filter(house__campaign=campaign, reaction='negative').count()
        total_contacts = ApartmentVisit.objects.filter(house__campaign=campaign).exclude(contact_name__isnull=True).count()

        houses_data = []
        for house in campaign.houses.all():
            house_visits = house.apartmentvisit_set.count()
            house_positive_reactions = house.apartmentvisit_set.filter(reaction='positive').count()
            house_neutral_reactions = house.apartmentvisit_set.filter(reaction='neutral').count()
            house_negative_reactions = house.apartmentvisit_set.filter(reaction='negative').count()
            house_contacts = house.apartmentvisit_set.exclude(contact_name__isnull=True).count()

            house_data = {
                'house_name': house.city,
                'total_visits': house_visits,
                'positive_reactions': house_positive_reactions,
                'neutral_reactions': house_neutral_reactions,
                'negative_reactions': house_negative_reactions,
                'total_contacts': house_contacts,
            }
            houses_data.append(house_data)

        campaign_data.append({
            'campaign_name': campaign.name,
            'total_visits': total_visits,
            'positive_reactions': positive_reactions,
            'neutral_reactions': neutral_reactions,
            'negative_reactions': negative_reactions,
            'total_contacts': total_contacts,
            'houses': houses_data,
        })

    context = {
        'campaign_data': campaign_data,
    }
    return render(request, 'campaign_statistics.html', context)
