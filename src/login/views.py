from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate

from login.forms import LoginForm


def sitelogin(request, orig_url):
        if request.user.is_authenticated():
                return HttpResponseRedirect('/' +orig_url)

        if not request.method == 'POST':
	        lform = LoginForm()
        	return render_to_response('login/login.html', { 'lform': lform })
	
        lform = LoginForm(request.POST)
        if not lform.is_valid():
                return render_to_response('login/error.html')

        username = lform.cleaned_data['username']
        password = lform.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user == None or not user.is_active:
                return render_to_response('login/error.html')
        login(request, user)
        return HttpResponseRedirect('/' +orig_url)
