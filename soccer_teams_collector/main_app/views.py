from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Teams
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
# Create your views here.


class Home(TemplateView):
    template_name = 'home.html'


class About(TemplateView):
    template_name = 'about.html'


class Team(TemplateView):
    template_name = 'index.html'


class Team:
    def __init__(self, name, image, country, stadium):
        self.name = name
        self.image = image
        self.country = country
        self.stadium = stadium


# teams = [Team("Galatasaray", "https://w7.pngwing.com/pngs/531/129/png-transparent-fenerbahce-s-k-dream-league-soccer-galatasaray-s-k-logo-football-football-text-sport-sports.png",
#               "Turkey", "Nef Stadium", "22 Turkish Premier League 🥇,18 Turkish Cup  🥇 , 1 UEFA Cup 🥇 , 1 UEFA Super Cup 🥇"),
#          Team("Galatasaray", "https://upload.wikimedia.org/wikipedia/commons/thumb/7/79/Galatasaray_4_Sterne_Logo.svg/1200px-Galatasaray_4_Sterne_Logo.svg.png",
#               "Turkey", "Nef Stadium", "22 Turkish Premier League 🥇,18 Turkish Cup  🥇 , 1 UEFA Cup 🥇 , 1 UEFA Super Cup 🥇"), Team("Galatasaray", "https://upload.wikimedia.org/wikipedia/commons/thumb/7/79/Galatasaray_4_Sterne_Logo.svg/1336px-Galatasaray_4_Sterne_Logo.svg.png",
#                                                                                                                                   "Turkey", "Nef Stadium", "22 Turkish Premier League 🥇,18 Turkish Cup  🥇 , 1 UEFA Cup 🥇 , 1 UEFA Super Cup 🥇")]


class TeamCreate(CreateView):
    model = Teams
    fields = ['name', 'image', 'country', 'stadium', 'honors']
    template_name = "team_create.html"
    success_url = "/teams/"


class TeamList(TemplateView):
    template_name = "team_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get(('name'))
        if name != None:
            context["teams"] = Teams.objects.filter(name__icontains=name)
            context["header"] = f"Searching for {name}"

        else:
            context["teams"] = Teams.objects.all()
            context["header"] = "Teams"
        return context


class TeamDetail(DetailView):
    model = Teams
    template_name = "team_details.html"


class TeamDelete(DeleteView):
    model = Teams
    template_name = 'team_delete_confirmation.html'
    success_url = "/teams/"


class TeamUpdate(UpdateView):
    model = Teams
    fields = ['name', 'image', 'country', 'stadium', 'honors']
    template_name = "team_update.html"
    success_url = "/teams/"
