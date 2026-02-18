# lab/hooks.py

from libqtile import hook
import subprocess
from lab.settings import wallpaper


@hook.subscribe.startup_once
def autostart():
    subprocess.Popen(["feh", "--bg-scale", wallpaper])
    subprocess.Popen(["emacs"])
    subprocess.Popen(["alacritty"])
    # subprocess.Popen(["picom"])
