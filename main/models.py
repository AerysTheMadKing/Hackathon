from django.db import models

from django.core.cache import cache
from account.models import CustomUser

RATE_CHOICE = (
    (1, 'ok'),
    (2, 'fine'),
    (3, 'good'),
    (4, 'amazing'),
    (5, 'incredible'),
)


class UserFilmRelation(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    films = models.ForeignKey('Film', on_delete=models.CASCADE)
    is_liked = models.BooleanField(default=False)
    is_bookmarks = models.BooleanField(default=False)
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICE)

    def __str__(self):
        return f'{self.user}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        cache.delete(f'film_{self.films.id}_rating')

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        cache.delete(f'film_{self.films.id}_rating')


class Film(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
    where_filmed = models.CharField(max_length=250)
    genre = models.CharField(max_length=200)
    cinema_company = models.CharField(max_length=150)
    director = models.CharField(max_length=160)
    year = models.DateField()
    user = models.ManyToManyField(CustomUser, through='UserFIlmRelation')
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=None, null=True, blank=True)
    price = models.DecimalField(max_digits=20, decimal_places=2, null=True)

    def __str__(self):
        return f'{self.director} {self.title}'

    def get_total_rating(self):
        # Check if rating is already in cache
        rating = cache.get(f'film_{self.id}_rating')
        if rating is not None:
            return rating

        # Calculate the rating if not in cache
        rating_sum = 0
        rating_count = 0
        user_relations = self.userfilmrelation_set.filter(rate__isnull=False)
        for relation in user_relations:
            rating_sum += relation.rate
            rating_count += 1

        # Calculate the average rating and cache the result for 1 day
        if rating_count > 0:
            rating = round(rating_sum / rating_count, 2)
            cache.set(f'film_{self.id}_rating', rating, timeout=86400)
            return rating
        else:
            return None
