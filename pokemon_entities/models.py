from django.db import models  # noqa F401

# your models here
class Pokemon(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название покемона")
    image = models.ImageField(upload_to="image/bulbazavr.png", verbose_name="Ваше изображение", null=True)

    def __str__(self):
        return self.title


class PokemonEntities(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name='entites', verbose_name="Ссылка на покемона")
    lat = models.FloatField(verbose_name="Широта покемона", null=True, blank=True)
    lon = models.FloatField(verbose_name="Долгота покемона", null=True, blank=True)
    appeared_at = models.DateTimeField(verbose_name="Дата появления", null=True)
    disappeared_at = models.DateTimeField(verbose_name="Дата исчезновения", null=True)