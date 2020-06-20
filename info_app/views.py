from django.shortcuts import render, redirect

# Create your views here.
def index(request):
  # if 'dojo' not in request.session:
  #   request.session['dojo'] = 'No place'
  context = {
    'name': request.session['name'],
    'loc': request.session['dojo'],
    'lang': request.session['lang']
  }
  return render(request, 'index.html', context)

def create(request):
  request.session['dojo'] = request.POST['dojo']
  request.session['name'] = request.POST['name']
  request.session['lang'] = request.POST['lang']
  return redirect('/')