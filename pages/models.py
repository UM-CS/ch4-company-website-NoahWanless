from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=200)
    #author = models.CharField(max_length=200)
    author = models.ForeignKey( #makes this element a forgin key, ie has to match with primary key of another table
        "auth.User",
        on_delete=models.CASCADE,
    )
    body = models.TextField()

    def __str__(self):
        return self.title
     
    def get_absolute_url(self): #for this post  reverse the full url name with this objects pk as the primary key in the url 
        return reverse("post_detail",kwargs={"pk":self.pk})


class Page(models.Model): #makes a tables with a textfield
    text=models.TextField()

    def __str__(self):
        return self.text[:50]


