# lab/groups.py

from libqtile.config import Group, Key
from libqtile.lazy import lazy
from lab.settings import mod

GROUPS = [
    ("1", ""),
    ("2", ""),
    ("3", ""),
    ("4", ""),
    ("5", "󰊱"),
    ("6", ""),
    ("7", "󰿈"),
    ("8", ""),
    ("9", "󱙧"),
    ("10", ""),
]

groups = [Group(name, label=label) for name, label in GROUPS]


def group_keys():
    keys = []
    for name, _ in GROUPS:
        keys.extend(
            [
                Key([mod], name[-1], lazy.group[name].toscreen()),
                Key([mod, "shift"], name[-1], lazy.window.togroup(name)),
            ]
        )
    return keys
