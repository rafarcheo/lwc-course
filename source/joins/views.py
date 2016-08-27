from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import EmailForm, JoinForm
from .models import Join

def get_ip(request):
	try: 
		x_forward = request.META.get("HTTP_X_FORWARED_FOR")
		if x_forward:
			ip = x_forward.split(",")[0]
		else:
			ip = request.META.get("REMOTE_ADDR")	
	except:
		ip = "brak"

	return ip			

import uuid
def get_ref_id():
	ref_id = str(uuid.uuid4())[:11].replace('-', '').lower()
	try:
		id_exists = Join.objectsget(ref_id=ref_id)
		get_ref_id()
	except:	
		return ref_id

def shere(request, ref_id):
	
	context = {"ref_id" : ref_id}
	templte = 'shere.html'
	return render(request, templte, context)


def home(request):
	try:
		join_id = request.session['join_id_ref']
		obj = Join.objects.get(id=join_id)
		print "the id is - " + str(join_id)
		print "the obj is %s" %(obj.email)
	except:
		join_id = None
		obj = None


		

	form = JoinForm(request.POST or None)
	join = Join.objects.all().order_by('ip_address').filter(ip_address="ABC")

	if form.is_valid():
		new_join = form.save(commit=False)
		email = form.cleaned_data['email']
		new_join_old, created = Join.objects.get_or_create(email=email)
		if created:
			new_join_old.ref_id = get_ref_id()
			new_join_old.ip_address = get_ip(request)
			new_join_old.save()
			return HttpResponseRedirect("/%s" %(new_join_old.ref_id))

	context = {
				'form': form,
				'joins': join,
			   }

	template = 'home.html'
	return render(request, template, context)