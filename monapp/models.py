from django.db import models

# Create your models here.

class Category(models.Model):
    nom=models.CharField(max_length=200)
    slug=models.SlugField(max_length=200)


    def _str_(self):
        return self.nom
    


class Portfolio(models.Model):
    categorie=models.ForeignKey(Category,on_delete=models.CASCADE, default=1)
    nom_client=models.CharField(max_length=200, help_text="Nom du client")
    tittre=models.CharField(max_length=200)
    slug=models.SlugField(max_length=200)
    image=models.ImageField(upload_to='média')
    image1=models.ImageField(upload_to='média')
    image2=models.ImageField(upload_to='média')
   
    description=models.TextField(default="")
    auteur=models.CharField(max_length=200, help_text="Auteur")
    date=models.DateTimeField(auto_now_add=True)


    def _str_(self):
        return self.tittre
    

class Contact(models.Model):
    nom=models.CharField(max_length=200)
    email=models.EmailField()
    sujet=models.CharField(max_length=500)
    description=models.TextField(default="")
    
    
    def _str_(self):
        return self.nom




class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    video = models.FileField(upload_to='videos/')
    video1 = models.FileField(upload_to='videos/')
    video2 = models.FileField(upload_to='videos/')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

