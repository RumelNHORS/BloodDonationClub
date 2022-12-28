from django.shortcuts import render, redirect
from . forms import RegisterForm, AddDonorModelForm
from django.views.generic.edit import CreateView
from . models import AddDonarModle
from django.contrib.messages.views import SuccessMessageMixin
#from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.list import ListView
#from django.contrib.auth import authenticate, login, logout
from django.http import Http404

#Paginator Stuff for function based view
from django.core.paginator import Paginator

# Create your views here.

def HomeView(request):
    return render(request, 'myapp/base.html')

def RegisterView(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("/login")
    else:
        form = RegisterForm()
    return render(response, "registration/register.html", {'form':form})

class AddDonorView(CreateView, SuccessMessageMixin):
    #model = AddDonarModle
    form_class = AddDonorModelForm
    template_name = 'myapp/add_donor.html'
    success_url = '/add_donor/'
    success_message = "%(name)s was created successfully"

class DonorListView(ListView):
    model = AddDonarModle
    template_name = 'myapp/show_donor.html'
    ordering = ['name']
    context_object_name = 'donor_list'
    #paginator stuff
    paginate_by = 3
    paginate_orphans = 1
    
    def get_context_data(self, *args, **kwargs):
        try:
            return super(DonorListView, self).get_context_data(*args, **kwargs)
        except Http404:
            self.kwargs['page'] = 1
            return super(DonorListView, self).get_context_data(*args, **kwargs)

def SearchDonor(request):
    if request.method == "POST":
        searched = request.POST['searched']
        search_result = AddDonarModle.objects.filter(blood_group__contains=searched)
        search_result_address = AddDonarModle.objects.filter(address__contains=searched)
        
        #paginator for function based view
        paginator = Paginator(search_result, 3)
        page_number = request.GET.get('page')
        final = paginator.get_page(page_number)
        
        context = {
            'searched': searched,
            'search_result': search_result,
            'search_result_address': search_result_address,
            'final': final
        }
        return render(request, 'myapp/search_donor.html', context)
    else:
        return render(request, 'myapp/search_donor.html', {})
