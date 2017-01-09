from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from .models import Histograph, SignUp
from django.core.context_processors import csrf
from .forms import SignUpForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import csv
from django.utils.encoding import smart_str
from django.views.decorators.csrf import csrf_exempt  
from .serializers import SignUpSerializer




def index(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/newspaper/')
	else:
		form = SignUpForm()
	args = {}
	args.update(csrf(request))
	args['form'] = form
	template = "base.html"
	return render(request, template, args)

def graphultimate(request):
  all_results = Histograph.objects.all()
  print all_results
  return render_to_response('graph.html', {'all_results' : all_results})


def result(request):
	signups = SignUp.objects.all()
	paginator = Paginator(signups,4)
	page = request.GET.get('page')
	num_pages = paginator.num_pages
	try:
		signups = paginator.page(page)
	except PageNotAnInteger:
		signups = paginator.page(1)
	except EmptyPage:
		signups = paginator.page(paginator.num_pages)
	args = {} 
	args.update(csrf(request))
	args['signups'] = signups
	args['num_pages'] = range(num_pages)
	template = "result.html"
	return render(request, template, args)

def detail(request,signup_id):
	try:
		signup = SignUp.objects.get(pk=signup_id)
	except SignUp.DoesNotExist:
		raise Http404("Signup does not exist")
	args={}
	template = "detail.html"
	args['signup'] = signup
	return render(request, template, args)

def update(request, signup_id):
	instance = SignUp.objects.get(pk=signup_id)
	form = SignUpForm(request.POST or None, instance=instance)
	if form.is_valid():
		form.save()
		messages.success(request, 'Profile details updated.')
		return HttpResponseRedirect('/newspaper/update/{}' .format(signup_id))
	args={}
	args['form'] = form
	template = "update.html"	
	return render(request, template, args)


@csrf_exempt
def export_csv(request):
	queryset = SignUp.objects.all()
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename=Signup.csv'
	print "working on request"
	print queryset
	writer = csv.writer(response, csv.excel)
	response.write(u'\ufeff'.encode('utf8'))
	writer.writerow([
		smart_str(u"First Name"),
		smart_str(u"Last Name"),
		smart_str(u"Email"),
		])
	for obj in queryset:
		writer.writerow([
			smart_str(obj.first_name),
			smart_str(obj.last_name),
			smart_str(obj.email),
			])
	return response

def search(request):
	if request.method == 'POST':
		search_text = request.POST.get('search_text')
	else:
		search_text = ''
	if search_text is not None:
		signups = SignUp.objects.filter(first_name__startswith=search_text)
	args = {}
	args['signups'] = signups
	template = 'ajax_search.html'
	return render_to_response(template, args)


from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from newspaper.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer	
    

class SignUpViewSet(viewsets.ModelViewSet):
	queryset = SignUp.objects.all()
	serializer_class = SignUpSerializer
	pagination_class = None


def angular(request):
	args={}
	template = "angular.html"
	return render(request, template, args)