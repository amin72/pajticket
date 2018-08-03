from django.shortcuts import render
from django.db.models import Q
from itertools import chain

from tickets.models import Film, Theater, Concert


def search(request):
    q = request.GET.get('q')
    film_theater_query = ( Q(title__icontains=q) |
                           Q(director__person__first_name__icontains=q) |
                           Q(director__person__last_name__icontains=q) )

    films = Film.objects.filter(film_theater_query)
    theaters = Theater.objects.filter(film_theater_query)
    
    concert_query = (Q(title__icontains=q) |
                     Q(artist__first_name__icontains=q) |
                     Q(artist__last_name__icontains=q))
    concerts = Concert.objects.filter(concert_query)

    return render(request, 'search/search.html', {
        'films': films,
        'theaters': theaters,
        'concerts': concerts
    })
