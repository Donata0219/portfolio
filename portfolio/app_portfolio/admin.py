from django.contrib import admin
from .models import Profilis, Projektai


# @admin.register(Profilis)
class ProfilisAdmin(admin.ModelAdmin):
    list_display = (
        'vardas',
        'pavarde',
        'trumpas_prisistatymas',
        'socialinis_tinklas_linkedin',
        'socialinis_tinklas_github'
    )


# @admin.register(Projektai)
class ProjektaiAdmin(admin.ModelAdmin):
    list_display = (
        'pavadinimas',
        'aprasymas',
        'technologiju_sarasas',
        'nuoroda_i_svetaine',
        'nuoroda_i_githuba',
        # 'created_at',
        # 'updated_at'
    )

admin.site.register(Profilis, ProfilisAdmin)
admin.site.register(Projektai, ProjektaiAdmin)

