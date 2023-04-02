from django.db.models import Avg, Sum

from main.models import UserFilmRelation, Film

from django.core.cache import cache

def get_total_rating(film_id):
    rating = cache.get(f'film_{film_id}_rating')
    if rating is not None:
        return rating

    try:
        film = Film.objects.get(id=film_id)
        rating_sum = film.userfilmrelation_set.aggregate(Sum('rate'))['rate__sum']
        rating_count = film.userfilmrelation_set.count()
        rating = round(rating_sum / rating_count, 2)
    except (Film.DoesNotExist, TypeError, ZeroDivisionError):
        rating = None

    cache.set(f'film_{film_id}_rating', rating, timeout=60 * 60 * 24)

    return rating