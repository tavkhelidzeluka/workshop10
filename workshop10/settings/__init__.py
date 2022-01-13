from time import monotonic
from workshop10.settings.common import *


try:
    from workshop10.settings.production import *
except ModuleNotFoundError:
    from workshop10.settings.local import * 
