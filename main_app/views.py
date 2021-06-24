from django.shortcuts import render
from .models import Cat, CatToy
# add these lines to the imports at the top
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

class CatCreate(CreateView):
  model = Cat
  fields = ['name', 'breed', 'description', 'age', 'cattoys']
  success_url = '/cats'

  def form_valid(self, form):
    self.object = form.save(commit=False)
    self.object.user = self.request.user
    self.object.save()
    return HttpResponseRedirect('/cats')

class CatUpdate(UpdateView):
  model = Cat
  fields = ['name', 'breed', 'description', 'age', 'cattoys']

  def form_valid(self, form):
    self.object = form.save(commit=False)
    self.object.save()
    return HttpResponseRedirect('/cats/' + str(self.object.pk))

class CatDelete(DeleteView):
  model = Cat
  success_url = '/cats'

# Create your views here.
def about(request):
    return render(request, 'about.html')

def index(request):
    return render(request, 'index.html')

def cats_index(request):
        cats = Cat.objects.all()
        return render(request, 'cats/index.html', { 'cats':cats })

def cats_show(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    return render(request, 'cats/show.html', {'cat': cat})

def profile(request, username):
    user = User.objects.get(username=username)
    cats = Cat.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, 'cats': cats})

def cattoys_index(request):
    cattoys = CatToy.objects.all()
    return render(request, 'cattoys/index.html', {'cattoys': cattoys})

def cattoys_show(request, cattoy_id):
    cattoy = CatToy.objects.get(id=cattoy_id)
    return render(request, 'cattoys/show.html', {'cattoy': cattoy})

class CatToyUpdate(UpdateView):
    model = CatToy
    fields = ['name', 'color']
    success_url = '/cattoys'

class CatToyDelete(DeleteView):
    model = CatToy
    success_url = '/cattoys'