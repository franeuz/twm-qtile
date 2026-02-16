# lab/keys.py

from libqtile.config import Key
from libqtile.lazy import lazy
from lab.settings import mod, emacs, terminal, browser, launcher, launcher_window

keys = [
    # Terminal
    Key([mod], "Return", lazy.spawn(terminal)),
    # Cerrar ventana
    Key([mod, "shift"], "q", lazy.window.kill()),
    # Fullscreen
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    # Floating
    Key([mod, "shift"], "space", lazy.window.toggle_floating()),
    # Cambiar layout
    Key([mod], "e", lazy.next_layout()),
    # Foco (hjkl + flechas)
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "l", lazy.layout.right()),
    # Mover ventanas
    Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()),
    # Resize (equivalente al mode resize)
    Key([mod], "r", lazy.layout.grow()),
    Key([mod, "shift"], "r", lazy.layout.shrink()),
    # Apps
    Key([mod, "shift"], "e", lazy.spawn(emacs)),
    Key([mod, "shift"], "v", lazy.spawn(browser)),
    Key([mod], "d", lazy.spawn(launcher)),
    Key([mod, "shift"], "d", lazy.spawn(launcher_window)),
    # Sistema
    Key([mod, "shift"], "c", lazy.reload_config()),
    Key([mod, "shift"], "r", lazy.restart()),
    Key([mod, "mod1"], "s", lazy.spawn("/sbin/poweroff")),
    # Capturas
    Key(
        [],
        "Print",
        lazy.spawn("scrot /home/franz/Imágenes/capturas/%Y-%m-%d_%H-%M-%S.png"),
        desc="Screenshot completo",
    ),
    Key(
        ["shift"],
        "Print",
        lazy.spawn("scrot -s /home/franz/Imágenes/capturas/%Y-%m-%d_%H-%M-%S.png"),
        desc="Screenshot selección",
    ),
]
