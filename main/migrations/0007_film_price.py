# Generated by Django 4.1.7 on 2023-04-01 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_userfilmrelation_unique_together_film_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=20, null=True),
        ),
    ]