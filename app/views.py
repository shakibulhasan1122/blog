from django.views.generic import ListView,DetailView,TemplateView
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login,logout
from django.core.paginator import Paginator
from django.db.models import Q
from . forms import ArticleForm,UserRegisterForm,WriterNameForm
from . models import ArticleCategory
from . models import Story
from . models import  AuthorView
from . models import AuthorName

def HomeView(request):
    if request.user.is_authenticated:
        articles=Story.objects.all()
        paginator=Paginator(articles,4)
        page=request.GET.get('page')

        articles=paginator.get_page(page)
        context={'articles':articles}
        return render(request,'home.html',context)
    else:
        return redirect('login')
    return render(request,'login.html')     

def AuthorViews(request):     
    if request.user.is_authenticated:
        authors=AuthorView.objects.all()
        context={'authors':authors}
        return render(request,'author.html',context)
    else:
        return redirect('login')
    return render(request,'login.html')



class ArticleCategoryDetail(DetailView):
    model=Story
    model=ArticleCategory
    template_name='cat_detail.html'
    context_object_name='cat'

class ArticleDetailView(DetailView):
    model=Story
    template_name='detail.html'
    context_object_name= 'gaitonde'

class AuthorDetailView(DetailView):
    model= AuthorView
    template_name='au_detail.html'
    context_object_name='writer'
 
    
def GetLogin(request):
    if request.user.is_authenticated:
        return redirect('Home')
    else:
        if request.method=="POST":
            user=request.POST.get('user')
            password=request.POST.get('pass')
            auth=authenticate(request,username=user,password=password)
            if auth is not None:
                login(request,auth)
                return redirect('Home')
            else:
                return redirect('login')

    return render(request,"login.html")

def GetLogout(request):
    if request.user.is_authenticated:    
        logout(request)
        return redirect('login')    
    else:
        return redirect('login')    
  
class SearchView(ListView):
    model=Story
    template_name='search.html'

    def get_queryset(self):
        query=self.request.GET.get('q')
        object_list=Story.objects.filter(
            Q(title__icontains=query)|Q(story__icontains=query)
        )
        return object_list

def CreateAritcle(request):
    form=ArticleForm()
    if request.user.is_authenticated:
        if request.method== "POST":
            form=ArticleForm(request.POST)
            if form.is_valid():
                form.save()
    else:
        return redirect('login')            
    context={'form':form}
    return render(request,'createpost.html',context)


def SignUp(request):
    form=UserRegisterForm
    if request.user.is_authenticated:
        return redirect('Home')
    else:    
        if request.method== "POST":
                form=UserRegisterForm(request.POST)
                if form.is_valid():
                    form.save()    
    context={'form':form}
    return render(request,'signup.html',context)