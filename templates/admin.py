# -*- encoding: utf-8 -*-
from django.contrib import admin
from furnas.models import Usuario, Trabalhador, Nutricionista, Avaliador, Administrador, UF, Raca, Genero, EstadoCivil, Escolaridade, Unidade, AreaAtuacao, Setor, Cargo, TurnoTrabalho
from furnas.models import AvaliacaoFisica, Anamnese, ObjetivosExercicio, MedidasAntropometricas, AvaliacaoPostural, FlexiTeste, ItemFlexiTeste, Whoqol
from furnas.models import AvaliacaoNutricional, HPP, HistoriaFamiliar, HistoriaFamiliarDoenca, HistoriaSocial, HabitosNutricionais, RelatorioRecordatorio, Recordatorio, ItemRecordatorio, Alimento, MedidaCaseira, PesosMedidas, Taco, ResultadoRefeicao

# Classes para exibição no Admin
class AlimentoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'tipo', 'preparo', ]
    list_filter = ['nome', 'tipo', 'preparo', ]

# Sistema
admin.site.register(Usuario)
admin.site.register(Trabalhador)
admin.site.register(Nutricionista)
admin.site.register(Avaliador)
admin.site.register(Administrador)
admin.site.register(UF)
admin.site.register(Raca)
admin.site.register(Genero)
admin.site.register(EstadoCivil)
admin.site.register(Escolaridade)
admin.site.register(Unidade)
admin.site.register(AreaAtuacao)
admin.site.register(Setor)
admin.site.register(Cargo)
admin.site.register(TurnoTrabalho)
# Avaliação Física
admin.site.register(AvaliacaoFisica)
admin.site.register(Anamnese)
admin.site.register(ObjetivosExercicio)
admin.site.register(MedidasAntropometricas)
admin.site.register(AvaliacaoPostural)
admin.site.register(FlexiTeste)
admin.site.register(ItemFlexiTeste)
admin.site.register(Whoqol)
# Avaliação Nutricional
admin.site.register(AvaliacaoNutricional)
admin.site.register(HPP)
admin.site.register(HistoriaFamiliar)
admin.site.register(HistoriaFamiliarDoenca)
admin.site.register(HistoriaSocial)
admin.site.register(HabitosNutricionais)
admin.site.register(RelatorioRecordatorio)
admin.site.register(Recordatorio)
admin.site.register(ItemRecordatorio)
admin.site.register(Alimento, AlimentoAdmin)
admin.site.register(MedidaCaseira)
admin.site.register(PesosMedidas)
admin.site.register(Taco)
admin.site.register(ResultadoRefeicao)
