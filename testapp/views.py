from django.shortcuts import render
from django.contrib.auth.decorators import login_required
#from testapp.forms import signupForm
from testapp.forms import signupForm
from django.http import HttpResponseRedirect

# Create your views here.
def homepage_view(request):
    return render(request, 'testapp/home.html')

def language_view_page_view(request):
    return render(request, 'testapp/language.html')

def dbms_page_view(request):
    return render(request, 'testapp/dbms.html')

def cn_page_view(request):
    return render(request, 'testapp/cn.html')

def se_page_view(request):
    return render(request, 'testapp/se.html')

def ai_page_view(request):
    return render(request, 'testapp/ai.html')

def dmi_page_view(request):
    return render(request, 'testapp/dmi.html')

def cc_page_view(request):
    return render(request, 'testapp/cc.html')

def dm_page_view(request):
    return render(request, 'testapp/dm.html')

def em_page_view(request):
    return render(request, 'testapp/em.html')

def toc_page_view(request):
    return render(request, 'testapp/toc.html')

def comc_page_view(request):
    return render(request, 'testapp/comc.html')

@login_required
def quiz_page_view(request):
    return render(request, 'testapp/quiz.html')

def logout_view(request):
    return render(request, 'testapp/logout.html')

def signup_view(request):
    form = signupForm()
    if request.method == 'POST':
        form = signupForm(request.POST)
        user = form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request, 'testapp/signup.html', {'form' : form} )
