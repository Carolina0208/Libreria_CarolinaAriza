from .Funciones import (
    # SELECCIÓN
    seleccion_torneo,
    seleccion_aleatoria,
    seleccion_ruleta,
    seleccion_ranking,
    seleccion_elitista,
    # CRUCE
    cruce_un_punto,
    cruce_dos_puntos,
    cruce_uniforme,
    cruce_aritmetico,
    # MUTACIÓN
    mutacion_binaria,
    mutacion_swap,
    mutacion_gaussiana
)
__all__ = [
    # SELECCIÓN
    'seleccion_torneo',
    'seleccion_aleatoria',
    'seleccion_ruleta',
    'seleccion_ranking',
    'seleccion_elitista',

    # CRUCE
    'cruce_un_punto',
    'cruce_dos_puntos',
    'cruce_uniforme',
    'cruce_aritmetico',

    # MUTACIÓN
    'mutacion_binaria',
    'mutacion_swap',
    'mutacion_gaussiana'
]