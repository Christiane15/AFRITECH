from django.db import models

class Intervention(models.Model):
    # Informations Client
    nom_client = models.CharField(max_length=100, verbose_name="Nom du client")
    tel_client = models.CharField(max_length=20, verbose_name="Numéro de téléphone")

    # Informations Appareil
    marque = models.CharField(max_length=50, verbose_name="Marque")
    type_appareil = models.CharField(max_length=100, verbose_name="Type d'appareil (TV, Drone, etc.)")
    panne_constatee = models.TextField(verbose_name="Panne constatée")

    # Gestion Technique (Cahier des charges)
    technicien_en_charge = models.CharField(max_length=100, verbose_name="Technicien assigné")
    composants_changes = models.TextField(blank=True, verbose_name="Composants/Pièces changés")
    cout_pieces = models.DecimalField(max_digits=10, decimal_places=0, default=0, verbose_name="Coût total des pièces (FCFA)")

    # Finances
    prix_devis = models.DecimalField(max_digits=10, decimal_places=0, null=True, blank=True, verbose_name="Prix du devis (FCFA)")    
    avance_versee = models.DecimalField(max_digits=10, decimal_places=0, default=0, null=True, blank=True, verbose_name="Avance versée (FCFA)")

    # Suivi
    date_creation = models.DateTimeField(auto_now_add=True, verbose_name="Date d'arrivée")
    statut = models.CharField(max_length=50, choices=[
        ('En attente', 'En attente'),
        ('En cours', 'En cours'),
        ('Prêt', 'Prêt'),
        ('Terminé', 'Terminé')
    ], default='En attente')

    def __str__(self):
        return f"{self.nom_client} - {self.type_appareil} ({self.marque})"
    
    def duree_en_atelier(self):
        if self.statut in ['En attente', 'En cours']:
            delta = timezone.now() - self.date_creation
            return delta.days 
    duree_en_atelier.short_description = "Jours en atelier"

    def lien_whatsapp(self):
        return f"https://wa.me/{self.tel_client}?text=Bonjour, votre {self.type_appareil} est {self.statut} chez AFRITECH."

    def __str__(self):
        return f"{self.nom_client} - {self.type_appareil} ({self.marque})"


    
