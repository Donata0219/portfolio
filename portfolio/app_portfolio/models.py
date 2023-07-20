from django.db import models


class Profilis(models.Model):
    vardas = models.CharField(max_length=100)
    pavarde = models.CharField(max_length=100)
    trumpas_prisistatymas = models.TextField()
    logotipas = models.ImageField(upload_to='logotipai/')
    socialinis_tinklas_linkedin = models.URLField(blank=True)
    socialinis_tinklas_github = models.URLField(blank=True)

    class Meta:

        # kad rodytų tvarkingus lietuviškus pavadinimus
        verbose_name = "Profilis"
        verbose_name_plural = "Profiliai"
    def __str__(self):
        return f"{self.vardas} {self.pavarde}"

class Projektai(models.Model):
    iliustracijos = models.ImageField(blank=True)
    pavadinimas = models.CharField(max_length=100)
    aprasymas = models.TextField()
    technologiju_sarasas = models.TextField()
    nuoroda_i_svetaine = models.URLField(blank=True)
    nuoroda_i_githuba = models.URLField(blank=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    class Meta:

        # kad rodytų tvarkingus lietuviškus pavadinimus
        verbose_name = "Projektas"
        verbose_name_plural = "Projektai"
    def __str__(self):
        return f"{self.pavadinimas} {self.aprasymas}"