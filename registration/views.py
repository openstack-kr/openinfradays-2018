from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect

from .email import send_email
from .forms import RegistrationForm, InviteForm, RegistrationCheckForm, RegistrationInfoForm
from .models import InviteCode, Registration


def payment_index(request):
    pass


def register_invite_ticket(request):
    form = RegistrationForm(request.POST)

    if not form.is_valid():
        return render(request, 'purchase.html',
                      {'title': '초청 티켓 등록', 'form': form})
    invite_code = form.cleaned_data.get('invite_code')
    email = form.data.get('email')
    name = form.cleaned_data.get('name')
    duty = form.cleaned_data.get('duty')
    company = form.cleaned_data.get('company')
    team = form.cleaned_data.get('team')
    phone = form.cleaned_data.get('phone_number')
    company_phone = form.cleaned_data.get('company_phone_number')
    term_agreed = form.cleaned_data.get('term_agreed')
    participant_dates = form.cleaned_data.get('participant_dates')

    try:
        code = InviteCode.objects.get(code=invite_code)
    except Exception:
        return redirect('invite')

    try:
        Registration.objects.get(invite_code=invite_code)
        return redirect('invite')
    except ObjectDoesNotExist as e:
        pass
    except Exception:
        return redirect('invite')

    registration = Registration(
        name=name,
        email=email,
        company=company,
        duty=duty,
        phone_number=phone,
        invite_code=invite_code,
        company_phone_number=company_phone,
        team=team,
        term_agreed=term_agreed,
        participant_dates=participant_dates,
    )
    registration.save()
    code.user = registration
    code.save()
    d = {'day1': '1일차', 'day2': '2일차', 'both': '양일'}
    send_email(name, d[participant_dates], email)
    return render(request, 'registered.html')


def check(request):
    form = RegistrationCheckForm()
    if request.method == "POST":
        form = RegistrationCheckForm(request.POST or None)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            registration = Registration.objects.get(email=email)
            form = RegistrationInfoForm(initial={
                'invite_code': registration.invite_code,
                'email': registration.email,
                'name': registration.name,
                'duty': registration.duty,
                'team': registration.team,
                'company': registration.company,
                'phone_number': registration.phone_number,
                'participant_dates': registration.participant_dates
            })
            return render(request, 'purchase.html',
                          {'title': '티켓 정보', 'form': form})
    return render(request, 'invite.html',
                  {'title': '등록 확인',
                   'url': '/registration/check',
                   'form': form})


def invite(request):
    form = InviteForm()
    if request.method == "POST":
        form = InviteForm(request.POST or None)
        if form.is_valid():
            form = RegistrationForm(initial={'invite_code': form.cleaned_data['code']})
            return render(request, 'purchase.html',
                          {'title': '초청 티켓 등록', 'form': form})
    return render(request, 'invite.html',
                  {'title': '초청 코드 확인',
                   'url': '/registration/invite',
                   'form': form})
