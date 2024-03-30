from django.db import models
from django.shortcuts import render

# Create your models here.



class Category(models.Model):
    nom=models.CharField(max_length=200)
    slug=models.SlugField(max_length=200)


    def _str_(self):
        return self.nom
    


class Blog(models.Model):
    categorie=models.ForeignKey(Category,on_delete=models.CASCADE, default=1)
    nom_client=models.CharField(max_length=200, help_text="Nom du client")
    tittre=models.CharField(max_length=200)
    slug=models.SlugField(max_length=200)
    
    image1=models.ImageField(upload_to='média')
    image2=models.ImageField(upload_to='média')
    description=models.TextField(default="")
    fichier_video = models.FileField(upload_to='videos/',blank=True)
    auteur=models.CharField(max_length=200, help_text="Auteur")
    date=models.DateTimeField(auto_now_add=True)


    def _str_(self):
        return self.tittre
    