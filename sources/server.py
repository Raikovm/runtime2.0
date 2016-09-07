#!/usr/bin/python

import startup.server
import settings
import managers

from logs import VDOM_log_manager
from storage import VDOM_storage
from file_access import VDOM_file_manager # VDOM_share
from request import VDOM_request_manager
from resource import VDOM_resource_manager, VDOM_resource_editor
from database import VDOM_database_manager
from security import VDOM_user_manager, VDOM_acl_manager
from scripting import VDOM_compiler, VDOM_dispatcher
from memory import VDOM_memory
from engine import VDOM_engine

from server import VDOM_server
# from mailing import VDOM_email_manager
from session import VDOM_session_manager
from module import VDOM_module_manager


managers.register("log_manager", VDOM_log_manager)
managers.register("file_manager", VDOM_file_manager, lazy=True)
managers.register("storage", VDOM_storage, lazy=True)
# managers.register("file_share", VDOM_share, lazy=True)
managers.register("resource_manager", VDOM_resource_manager, lazy=True)
managers.register("database_manager", VDOM_database_manager, lazy=True)
managers.register("user_manager", VDOM_user_manager, lazy=True)
managers.register("acl_manager", VDOM_acl_manager, lazy=True)
managers.register("dispatcher", VDOM_dispatcher, lazy=True)
managers.register("compiler", VDOM_compiler, lazy=True)
managers.register("memory", VDOM_memory, lazy=True)
managers.register("engine", VDOM_engine, lazy=True)

managers.register("session_manager", VDOM_session_manager, lazy=True)
managers.register("request_manager", VDOM_request_manager, lazy=True)
managers.register("resource_editor", VDOM_resource_editor, lazy=True)
# managers.register("scheduler_manager", VDOM_scheduler_manager, lazy=True)
# managers.register("email_manager", VDOM_email_manager, lazy=True)
managers.register("module_manager", VDOM_module_manager)
managers.register("server", VDOM_server)


if settings.PRELOAD_DEFAULT_APPLICATION:
    managers.memory.applications.default


try:
    managers.server.start()
finally:
    if settings.PROFILING:
        from utils.profiling import profiler
        profiler.save()
