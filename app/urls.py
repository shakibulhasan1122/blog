from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.HomeView,name='Home'),
    path('author',views.AuthorViews,name='Author'),
    path('article/<int:pk>',views.ArticleDetailView.as_view(),name='article_page'),
    path('writer/<int:pk>',views.AuthorDetailView.as_view(),name='author_page'),
    path('login',views.GetLogin,name='login'),
    path('logout',views.GetLogout,name='logout'),
    path('searchresult',views.SearchView.as_view(),name='search_result'),
    path('create',views.CreateAritcle,name='create_article'),
    path('signup',views.SignUp,name='Sign_Up'),
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)