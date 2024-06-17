from django import forms
from .models import Player, Statistic

class StatisticForm(forms.ModelForm):
    class Meta:
        model = Statistic
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            # Al editar una estadística existente, permitir solo al jugador actual
            self.fields['player'].queryset = Player.objects.filter(pk=self.instance.player.pk)
        else:
            # Al crear una nueva estadística, excluir jugadores que ya tienen estadísticas
            self.fields['player'].queryset = Player.objects.exclude(statistics__isnull=False)