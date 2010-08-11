
from django.conf import settings
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect

import random, hashlib
from os.path import isfile, splitext


from f.models import File
from f.forms import UploadForm

def upload(request):
        if not request.user.is_authenticated():
                return HttpResponseRedirect('/login' +request.get_full_path())
	if not request.method == 'POST':
		return render_to_response('f/upload.html', {'form': UploadForm()})
	salt = hashlib.sha224(str(random.random())).hexdigest()[:5]
	key = hashlib.sha224(salt+request.user.username).hexdigest()[:6]

	ctrl=0
	while(ctrl <= 30):
		try:
			if ctrl == 30:
				return render_to_response('upload/error.html')
			File.objects.filter(key__exact=key)
			salt = hashlib.sha224(str(random.random())).hexdigest()[:5]
			key = hashlib.sha224(salt+request.user.username).hexdigest()[:6]
			break
		except:
			ctrl += 1
	destination = open(settings.MEDIA_ROOT+ '../shared/' +key+ splitext(request.FILES['f'].name)[1], 'wb+')
	for chunk in request.FILES['f'].chunks():
		destination.write(chunk)
	destination.close()
	f = File(f = request.FILES['f'].name, key = key, user = request.user)	
	f.save()
	return render_to_response('f/uploaded.html', {'key':key})

def download(request, key):
	f = get_object_or_404(File, key=key)
	return HttpResponseRedirect('/shared/'+key+ splitext(f.f.name)[1])
