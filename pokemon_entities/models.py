from django.db import models 


class Pokemon(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название покемона")
    title_en = models.CharField(max_length=200, verbose_name="Название покемона на английском", null=True, blank=True)
    title_jp = models.CharField(max_length=200, verbose_name="Название покемона на японском", null=True, blank=True)
    image = models.ImageField(upload_to="media/image/bulbazavr.png", verbose_name="Ваше изображение", null=True, blank=True)
    description = models.TextField(verbose_name="Описание покемона", null=True, blank=True)
    previous_evolution = models.ForeignKey("self", on_delete=models.CASCADE, related_name="next_evolution", verbose_name="Предыдущая эволюция покемона", blank=True, null=True)
    def __str__(self):
        return self.title


class PokemonEntities(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name='entites', verbose_name="Ссылка на покемона")
    lat = models.FloatField(verbose_name="Широта покемона", null=True)
    lon = models.FloatField(verbose_name="Долгота покемона", null=True)
    appeared_at = models.DateTimeField(verbose_name="Дата появления", null=True)
    disappeared_at = models.DateTimeField(verbose_name="Дата исчезновения", null=True)
    level = models.IntegerField(verbose_name="Уровень покемона", null=True, blank=True)
    health = models.IntegerField(verbose_name="Здоровье покемона", null=True, blank=True)
    attack = models.IntegerField(verbose_name="Атака покемона", null=True, blank=True)
    protection = models.IntegerField(verbose_name="Защита покемона", null=True, blank=True)
    stamina = models.IntegerField(verbose_name="Выносливость покемона", null=True, blank=True)
