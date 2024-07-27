from django.db import models

# Create your models here.

class Job(models.Model):
    title = models.CharField(max_length=200)  # Champ de texte pour le titre de l'offre d'emploi
    description = models.TextField()          # Champ de texte pour la description de l'offre
    location = models.CharField(max_length=100)  # Champ de texte pour la localisation de l'offre
    posted_date = models.DateTimeField(auto_now_add=True)  # Champ de date et heure, rempli automatiquement avec la date et l'heure actuelles lors de la création de l'enregistrement

    def __str__(self):
        return self.title  # Méthode pour retourner une représentation en chaîne de caractères de l'objet, ici le titre de l'offre