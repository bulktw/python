from django.shortcuts import render, get_object_or_404, redirect
#from django.http import HttpResponse
from .models import Allowlist
#from django.http import Http404
from .forms import AllowlistForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required

#def index(request):
#	return HttpResponse("Hello, World.")


#def list(request,employee_id):
#	return HttpResponse("Ur looking at Employee Number {id}.".format(id = employee_id))

def index(request):
	return render(request, 'index.html')

@login_required
def list(request):
	allow_list = Allowlist.objects.all().order_by('employeedept')
	return render(request, 'list.html', { 'allow_list': allow_list })

def detail(request, employee_id):
	#try:
	#	employee = Allowlist.objects.get(employeeid__exact=employee_id)
	#except Allowlist.DoesNotExist:
	#	raise Http404
	#return render(request, 'detail.html', { 'employee': employee })
	try:
		#__exact:精確符合
		employee = get_object_or_404(Allowlist, employeeid__exact=employee_id)
	except:
		return render(request, 'detail.html', { 'error_message': "查詢不到此工號的調查" })
	return render(request, 'detail.html', { 'employee': employee })

def submit(request):
	if request.method == 'POST':
		form = AllowlistForm(request.POST)
		if form.is_valid():
				employee = form.save(commit=False)
				employee.created_at = timezone.now()
				employee.save()
				return redirect('youtube:detail', employee_id=employee.employeeid)
	else:
		form = AllowlistForm()
	return render(request, 'submit.html', { 'form': form })

def edit(request, employee_id):
	employee = get_object_or_404(Allowlist, employeeid__exact=employee_id)
	if request.method == 'POST':
		form = AllowlistForm(request.POST, instance=employee)
		if form.is_valid():
			employee = form.save(commit=False)
			employee.created_at = timezone.now()
			employee.save()
			return redirect('youtube:detail', employee_id=employee.employeeid)		
	else:
		form = AllowlistForm(instance=employee)
	return render(request, 'edit.html', { 'form': form })

def remove(request, employee_id):
	employee = get_object_or_404(Allowlist, employeeid__exact=employee_id)
	employee.delete()
	return redirect('youtube:list')
	