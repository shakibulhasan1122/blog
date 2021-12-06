from django.forms import ModelForm
from. models import Story,AuthorName
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ArticleForm(ModelForm):
    class Meta:
        model=Story
        fields='__all__'

class UserRegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class WriterNameForm(ModelForm):
    class Meta:
        model=AuthorName
        fields='__all__'


        