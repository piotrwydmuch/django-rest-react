from django.http import HttpResponse
from django.views import generic

from .models import Advertisement

class IndexView(generic.ListView):
    template_name = "jobs/index.html"
    context_object_name = "advertisement_list"

    def get_queryset(self):
        return Advertisement.objects.order_by("-pub_date")
    
class DetailsView(generic.DetailView):
    model = Advertisement
    template_name = "jobs/details.html"