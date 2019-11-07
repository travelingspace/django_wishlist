from django.shortcuts import render
from .models import Place
from .forms import NewPlaceForm

# Create your views here.

def place_list(request):

    #handle post request to method and create the place
    if request.method == 'POST':
        form = NewPlaceForm(request.POST)
        place = form.save()
        if form.is_valid():
            place.save()
            return redirect('place_list')


    #when not a post request, just show the form with all unvistited places
    places = Place.objects.filter(visited=False).order_by('name')
    new_place_form = NewPlaceForm()
    return render(request, 'travel_wishlist/wishlist.html', {'places': places, 'new_place_form': new_place_form})