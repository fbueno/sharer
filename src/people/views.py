from django.contrib.auth import login, authenticate
from django.shortcuts import render_to_response, get_object_or_404
from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import HttpResponseRedirect


import random, hashlib, datetime

from django_mailman.models import List
from people.forms import RegForm, EmailForm
from people.models import Profile

def register(request):
    if not request.method == 'POST':
        return render_to_response('people/register.html', {'emailform': EmailForm() })

    maillist=List(name=settings.MAILLIST_NAME, password=settings.MAILLIST_PASSWORD, email=settings.MAILLIST_EMAIL, main_url=settings.MAILLIST_URL, encoding='iso-8859-1')
    ok = False
    for mail in maillist.get_all_members():
        if request.POST.get('email') in mail:
            ok = True
            break

    if not ok:
        return render_to_response('people/checkuser.html', {'error': True})

    user = User.objects.create_user(request.POST.get('email'), request.POST.get('email'), User.objects.make_random_password(length=8))
    user.is_active = False
    user.save()

    salt = hashlib.sha224(str(random.random())).hexdigest()[:5]
    activation_key = hashlib.sha224(salt+user.username).hexdigest()
    key_expires = datetime.datetime.today() + datetime.timedelta(2)

    profile = Profile(user = user, activation_key = activation_key, key_expires = key_expires)
    profile.save()


    email_subject = 'Confirmacao s.hal.vu'	
    email_body = 'Clica no link pra confirmar: http://s.hal.vu/confirm/'+profile.activation_key
    send_mail(email_subject, email_body,'admin@hal.vu',[user.email])
    return render_to_response('people/checkuser.html')


def confirm(request, key):
        user_profile = get_object_or_404(Profile,
                                 activation_key=key)
        if user_profile.key_expires < datetime.datetime.today():
                return render_to_response('people/error.html', {'expired': True})
        user_account = user_profile.user

        if user_account.is_active:
                return render_to_response('people/error.html', {'active': True})

        if not request.method == 'POST':
		form=RegForm()
		return render_to_response('people/confirm.html', {'form': form, 'key': key})
        form = RegForm(request.POST)
        if not form.is_valid():
                return render_to_response('people/formerror.html')
        user_account.set_password(form.cleaned_data['password'])
        user_account.is_active = True
        user_account.save()
        login(request, authenticate(username=user_account.username, password=form.cleaned_data['password']))
        return HttpResponseRedirect('/upload/')
