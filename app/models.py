from django.db import models

class ArticleCategory(models.Model):
    genre=models.CharField(max_length=100)

    def __str__(self):
        return self.genre



class Story(models.Model):
    title=models.CharField(max_length=100)
    story=models.TextField()
    
    article=models.ForeignKey(
        'ArticleCategory',
        on_delete=models.CASCADE
    )
    author=models.ForeignKey(
        'AuthorName',
        on_delete=models.CASCADE,
        default=None
    )
    def __str__(self):
        return self.title
  


class AuthorName(models.Model):
    a_name=models.CharField(max_length=100)    
    def __str__(self):
        return self.a_name

class AuthorView(models.Model):
    full_name=models.CharField(max_length=100,default=None)
    age=models.CharField(max_length=10)
    place=models.CharField(max_length=50)    

    author=models.ForeignKey(
        'AuthorName',
        on_delete=models.CASCADE,
        default=None
    )

    def __str__(self):
        return self.full_name