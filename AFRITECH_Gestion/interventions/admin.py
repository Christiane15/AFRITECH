from django.contrib import admin
from django.utils.html import format_html
from .models import Intervention 

@admin.register(Intervention)
class InterventionAdmin(admin.ModelAdmin):
    list_display = ('nom_client', 'type_appareil', 'technicien_en_charge', 'statut', 'duree_en_atelier', 'lien_whatsapp_link')
    list_filter = ('statut', 'technicien_en_charge')

    fieldsets = (
        ('CLIENT & APPAREIL', {
            'fields': ('nom_client', 'tel_client', 'type_appareil', 'marque', 'panne_constatee')
        }),
        ('TECHNIQUE & MAINTENANCE', {
            'fields': ('technicien_en_charge', 'composants_changes', 'cout_pieces')
        }),
        ('FINANCES & SUIVI', {
            'fields': ('prix_devis', 'avance_versee', 'statut')
        }),
    )

    def lien_whatsapp_link(self, obj):
        from django.utils.html import format_html
        return format_html('<a href="{}" target="_blank">Message</a>', obj.lien_whatsapp())
    lien_whatsapp_link.short_description = "WhatsApp"

