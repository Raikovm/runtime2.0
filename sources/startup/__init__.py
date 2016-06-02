
import __builtin__
import sys


# settings

from .importers.settings import SettingsFinder

finder = SettingsFinder()
sys.meta_path.append(finder)
settings = __import__("settings")
sys.meta_path.remove(finder)


# initialize

import utils.codecs
import utils.system
import utils.threads
import logs


# include modules and libraries to search

sys.path.append(settings.MODULES_LOCATION)
sys.path.append(settings.LIBRARIES_LOCATION)


# register libraries finder

from .importers.libraries import LibraryFinder

sys.meta_path.append(LibraryFinder())


# start log server

from logs import VDOM_log_server

if settings.START_LOG_SERVER:
    VDOM_log_server().start()


# obsolete

from .debug import debug, DebugFile

__builtin__.VDOM_CONFIG = settings.VDOM_CONFIG
__builtin__.VDOM_CONFIG_1 = settings.VDOM_CONFIG_1
__builtin__.system_options = {"server_license_type": "0", "firmware": "N/A", "card_state": "0", "object_amount": "0"}
__builtin__.debug = debug
__builtin__.debugfile = DebugFile()
__builtin__._ = lambda value: value
