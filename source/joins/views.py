from django.shortcuts import render

from .forms import EmailForm, JoinForm
from .models import Join

def home(request):
	form = JoinForm(request.POST or None)
	if form.is_valid():
		new_join = form.save()
		email = form.cleaned_data['email']
		new_join_old, created = Join.objects.get_or_create(email=email)
		# new_join.save()
		
	context = {'form': form}
	template = 'home.html'
	return render(request, template, context)