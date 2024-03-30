from django.contrib import admin

from .models import Category, Contact, Portfolio,Video

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email', 'sujet', 'description')  # Champs à afficher dans la liste
    search_fields = ('nom', 'email', 'sujet')  # Champs de recherche
    list_filter = ('sujet',)  # Filtres latéraux
    # Vous pouvez ajouter d'autres options de personnalisation ici

# Enregistrement du modèle Contact avec la classe ContactAdmin
admin.site.register(Contact, ContactAdmin)

admin.site.register(Category)
admin.site.register(Portfolio)
admin.site.register(Video)
