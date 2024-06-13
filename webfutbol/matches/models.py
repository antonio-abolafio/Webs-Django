from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre del Equipo")
    shield = models.ImageField(upload_to='shields/', verbose_name="Escudo")

    class Meta:
        verbose_name = "Equipo"
        verbose_name_plural = "Equipos"
        ordering = ['-name']

    def __str__(self):
        return self.name


class Match(models.Model):
    journey = models.CharField(max_length=100, verbose_name="Jornada")
    local_team = models.ForeignKey(Team, related_name='local_matches', on_delete=models.CASCADE, verbose_name="Equipo Local")
    visiting_team = models.ForeignKey(Team, related_name='visiting_matches', on_delete=models.CASCADE, verbose_name="Equipo Visitante")
    result = models.CharField(max_length=10, verbose_name="Resultado")
    date = models.DateTimeField(verbose_name="Fecha")

    class Meta:
        verbose_name = "Partido"
        verbose_name_plural = "Partidos"
        ordering = ['-date']

    def __str__(self):
        return f"{self.local_team} vs {self.visiting_team} ({self.date.strftime('%Y-%m-%d')})"