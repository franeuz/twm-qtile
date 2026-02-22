# lab/screens.py

from libqtile import bar, widget
from libqtile.config import Screen

# Configuración global para los widgets
my_fontsize = 16

widget_defaults = dict(
    font="terminus-font",
    fontsize=my_fontsize,
    padding=6,
)


def base_widgets():
    return [
        widget.GroupBox(
            disable_drag=True,
            highlight_method="line",
            rounded=False,
            fontsize=my_fontsize,  # Tamaño de los workspace
        ),
        widget.Spacer(),
        widget.WindowName(
            max_chars=220,
            fontsize=my_fontsize,  # Tamaño del nombre del medio en tupla WindowName
        ),
        widget.Spacer(),
        widget.Clock(
            format="%Y-%m-%d %H:%M",
            fontsize=my_fontsize,  # Tamaño del reloj dentro de tupla
        ),
    ]


screens = [
    Screen(
        top=bar.Bar(
            base_widgets(),
            size=30,
            opacity=1.0,
        ),
    ),
]
