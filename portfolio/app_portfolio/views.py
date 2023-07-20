from django.shortcuts import render

# class SkaitiklisView(View):
#     def get(self, request):
#         skaitikliai = Skaitiklis.objects.all()
#         return render(request, 'skaitikliai.html', {'skaitikliai': skaitikliai})

from django.shortcuts import render
from django.views import View
from .models import Profilis, Projektai


class ProfilisIrProjektaiView(View):
    def get(self, request):
        profilis = Profilis.objects.all()
        projektai = Projektai.objects.all()
        return render(request, 'app_portfolio/index.html', {'profilis': profilis, 'projektai': projektai})