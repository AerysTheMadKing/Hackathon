# Generated by Django 4.1.7 on 2023-03-30 04:50

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_remove_film_rate_userfilmrelation_film_user'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='userfilmrelation',
            unique_together={('user', 'films')},
        ),
    ]