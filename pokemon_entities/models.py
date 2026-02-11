from django.db import models  # noqa F401

# your models here
class Pokemon(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название покемона")

    def __str__(self):
        return self.title


class PokemonEntities(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name='entites', verbose_name="Ссылка на покемона")