from django.db import models
from datetime import date

# Create your models here.
class Player(models.Model):
    name = models.CharField(default="Jugador", max_length=100, verbose_name="Nombre")
    last_name = models.CharField(blank=True, null=True, max_length=100, verbose_name="Apellidos")
    soccer_number = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name="Dorsal")
    birthdate = models.DateField(blank=True, null=True, verbose_name="Fecha de nacimiento")
    profile = models.ImageField(upload_to="jugadores/", blank=True, null=True, verbose_name="Perfil")
    age = models.PositiveSmallIntegerField(default=0, blank=True, null=True, verbose_name="Edad")

    class Meta:
        verbose_name="Jugador"
        verbose_name_plural="Jugadores"
        ordering = ["-name"]

    def save(self, *args, **kwargs):
        self.age = self.calculate_age()
        super(Player, self).save(*args, **kwargs)

    def calculate_age(self):
        today = date.today()
        age = today.year - self.birthdate.year - ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))
        return age

    def __str__(self):
        return f'{self.name} {self.last_name}'


class Statistic(models.Model):
    player = models.ForeignKey(Player, default=None, on_delete=models.CASCADE, verbose_name="Estadísticas")
    games_played = models.PositiveSmallIntegerField(default=0, verbose_name="Partido Jugados")
    minutes_played = models.PositiveSmallIntegerField(default=0, verbose_name="Minutos")
    goals = models.PositiveSmallIntegerField(default=0, verbose_name="Goles")
    yellow_cards = models.PositiveSmallIntegerField(default=0, verbose_name="Tarjeas Amarillas")
    red_cards = models.PositiveSmallIntegerField(default=0, verbose_name="Tarjetas Rojas")

    def __str__(self):
        return f"{self.player.name}"
