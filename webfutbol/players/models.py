from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify
from django.db import models
from datetime import date


# Create your models here.
class Position(models.Model):
    name = models.CharField(max_length=50, verbose_name="Posición")

    class Meta:
        verbose_name = "Posición"
        verbose_name_plural = "Posiciones"

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(default="Jugador", max_length=100, verbose_name="Nombre")
    last_name = models.CharField(blank=True, null=True, max_length=100, verbose_name="Apellidos")
    alias = models.CharField(max_length=100, verbose_name="Alias")
    soccer_number = models.PositiveSmallIntegerField(default=0, verbose_name="Dorsal")
    position = models.ForeignKey(Position, blank=True, null=True, on_delete=models.CASCADE, verbose_name="Posicion")
    birthdate = models.DateField(default=date(1990, 1, 1), verbose_name="Fecha de nacimiento")
    profile = models.ImageField(upload_to="players/", default="players/usuario.png", blank=True, null=True, verbose_name="Perfil")
    age = models.PositiveSmallIntegerField(default=0, blank=True, null=True, verbose_name="Edad")
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        verbose_name = "Jugador"
        verbose_name_plural = "Jugadores"
        ordering = ["-name"]

    def save(self, *args, **kwargs):
        self.age = self.calculate_age()
        super(Player, self).save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(self.alias)
        super().save(*args, **kwargs)


    def calculate_age(self):
        today = date.today()
        age = today.year - self.birthdate.year - ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))
        return age

    def __str__(self):
        return f"{self.alias} {self.soccer_number}"


class Statistic(models.Model):
    player = models.OneToOneField(Player, default=None, on_delete=models.CASCADE, verbose_name="Estadísticas")
    games_played = models.PositiveSmallIntegerField(default=0, verbose_name="Partido Jugados")
    minutes_played = models.PositiveSmallIntegerField(default=0, verbose_name="Minutos")
    goals = models.PositiveSmallIntegerField(default=0, verbose_name="Goles")
    yellow_cards = models.PositiveSmallIntegerField(default=0, verbose_name="Tarjeas Amarillas")
    red_cards = models.PositiveSmallIntegerField(default=0, verbose_name="Tarjetas Rojas")

    class Meta:
        verbose_name = "Estadística"
        verbose_name_plural = "Estadísticas"

    def __str__(self):
        return self.name

    def __str__(self):
        return f"Estadísticas de {self.player}"


@receiver(post_save, sender=Player)
def create_or_update_statistic(sender, instance, created, **kwargs):
    if created:
        Statistic.objects.create(player=instance)
    else:
        instance.statistic.save()
