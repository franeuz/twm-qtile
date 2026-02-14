# Qtile minimal config

from lab.settings import *
from lab.keys import keys
from lab.groups import groups, group_keys
from lab.layouts import layouts
from lab.rules import *
from lab.screens import screens
import lab.hooks

keys.extend(group_keys())

wmname = "Qtile"
