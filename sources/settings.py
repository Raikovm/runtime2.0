
SERVER_ID = "5ED67D80-9017-4753-9633-685A1926A6B9"

# defaults

DEFAULT_LANGUAGE = "en"
DEFAULT_APPLICATION = None

# server

SERVER_ADDRESS = ""
SERVER_PORT = 80

# locations

if WINDOWS:

    REPOSITORY_LOCATION = "../data/repository"
    TYPES_LOCATION = "../types"
    APPLICATIONS_LOCATION = "../applications"
    RESOURCES_LOCATION = "../resources"
    CACHE_LOCATION = "../cache"
    DATA_LOCATION = "../data"
    TEMPORARY_LOCATION = "../temp"

else:

    REPOSITORY_LOCATION = "/var/vdom/repository"
    TYPES_LOCATION = "/var/vdom/types"
    APPLICATIONS_LOCATION = "/var/vdom/applications"
    RESOURCES_LOCATION = "/var/vdom/resources"
    CACHE_LOCATION = "/var/vdom/cache"
    DATA_LOCATION = "/var/vdom/data"
    TEMPORARY_LOCATION = "/tmp"


DATABASES_LOCATION = DATA_LOCATION + "/databases"
STORAGE_LOCATION = DATA_LOCATION + "/storage"
LOGS_LOCATION = TEMPORARY_LOCATION

SERVER_PIDFILE_LOCATION = TEMPORARY_LOCATION + "/server.pid"
LOGGER_PIDFILE_LOCATION = TEMPORARY_LOCATION + "/logger.pid"

# obsolete locations

LOCAL_LOCATION = "../local"
MODULES_LOCATION = LOCAL_LOCATION + "/modules"
LIBRARIES_LOCATION = LOCAL_LOCATION + "/libraries"

FONTS_LOCATION = "../fonts"

# memory

REPOSITORY_TYPES_SECTION = "types"
APPLICATION_FILENAME = "application.xml"
TYPE_FILENAME = "type.xml"
RESOURCE_LINE_LENGTH = 76
ALLOW_TO_CHANGE = "00000000-0000-0000-0000-000000000000"
AUTOSAVE_APPLICATIONS = True

# sessions

SESSION_LIFETIME = 1200

# timeouts

SCRIPT_TIMEOUT = 30.1
COMPUTE_TIMEOUT = 30.1
RENDER_TIMEOUT = 30.1
WYSIWYG_TIMEOUT = 30.1

# threading

QUANTUM = 0.5
COUNTDOWN = 3.0
MAIN_NAME = "Main"

# logging

if SERVER:
    LOGGING = True
    if WINDOWS:
        START_LOG_SERVER = True
    else:
        START_LOG_SERVER = False
else:
    LOGGING = False
    START_LOG_SERVER = False

LOGGING_ADDRESS = "127.0.0.1"
LOGGING_PORT = 1010

LOGGING_TIMESTAMP = "%Y-%m-%d %H:%M:%S"

LOGGING_AUTOMODULE = True
LOGGING_OUTPUT = True
DISPLAY_WARININGS_ANYWAY = True
DISPLAY_ERRORS_ANYWAY = True

# watcher

WATCHER = True
WATCHER_ADDRESS = "127.0.0.1"
WATCHER_PORT = 1011

# vscript

DISABLE_VSCRIPT = 0
OPTIMIZE_VSCRIPT_PARSER = 0

# emails

SMTP_SENDMAIL_TIMEOUT = 20.0
SMTP_SERVER_ADDRESS = ""
SMTP_SERVER_PORT = 25
SMTP_SERVER_USER = ""
SMTP_SERVER_PASSWORD = ""

# legacy

VDOM_CONFIG = {
    "SERVER-ID": SERVER_ID, # "5ED67D80-9017-4753-9633-685A1926A6B9"
    "DEFAULT-LANGUAGE": DEFAULT_LANGUAGE, # "en"
    # "HTTP-ERROR-PAGES-DIRECTORY": "../errors",

    # managers directories
    "FILE-ACCESS-DIRECTORY": LOCAL_LOCATION, # "../app"
    # "XML-MANAGER-DIRECTORY": "../app"
    # "APPLICATION-XML-TEMPLATE": "../app/app_template.xml"
    "SOURCE-MODULES-DIRECTORY": MODULES_LOCATION, # "../app/objects"

    # server stuff
    "SERVER-ADDRESS": SERVER_ADDRESS, # ""
    "SERVER-PORT": SERVER_PORT, # 80
    "WATCHER-PORT": WATCHER_PORT,
    # "SERVER-LOCALHOST-PORT": 2222,
    # "VDOM-MEMORY-SERVER-PORT": 3333,
    # "LOCALHOST-CARD-PORT": 4444,
    # "LOCALHOST-LOGGER-PORT": 5555,
    "SERVER-PIDFILE": SERVER_PIDFILE_LOCATION, # "../app/server.pid"
    "LOGGER-PIDFILE": LOGGER_PIDFILE_LOCATION, # "../app/logger.pid"
    # "SERVER-SOURCE-MANAGER-MEMORY-QUOTE": "10240",
    "AUTO-REMOVE-INCORRECT-APPLICATIONS": 0,

    # special URLs
    # "SOAP-POST-URL": "/SOAP",
    "MANAGEMENT-URL": "/system",
    # "WSDL-FILE-URL": "/vdom.wsdl",
    # "WSDL-FILE-LOCATION": "../app/vdom.wsdl",

    # "SOURCE-TYPES-LOCATION": "../types",
    "TYPES-LOCATION": TYPES_LOCATION, # "../app/types"

    # log
    "LOG-FILE-SIZE": 500000, # size of one log file
    "LOG-FILE-COUNT": 10, # max number of log files to store (history)

    # session stuff
    "SESSION-LIFETIME": SESSION_LIFETIME, # 1200

    # timeouts
    "SCRIPT-TIMEOUT": SCRIPT_TIMEOUT, # 30.1
    "COMPUTE-TIMEOUT": COMPUTE_TIMEOUT, # 30.1
    "RENDER-TIMEOUT": RENDER_TIMEOUT, # 30.1
    "WYSIWYG-TIMEOUT": WYSIWYG_TIMEOUT, # 30.1

    # "APP-SAVE-TIMEOUT": MEMORY_WRITER_QUANTUM, # 30.1

    "STORAGE-DIRECTORY": LOCAL_LOCATION, # "../app"
    "TEMP-DIRECTORY": TEMPORARY_LOCATION, # "../app/temp"
    "FONT-DIRECTORY": FONTS_LOCATION, # "../fonts"
    # "BACKUP-DIRECTORY": "../app/backup",
    # "SHARE-DIRECTORY": "../app/share",
    "FILE-STORAGE-DIRECTORY": STORAGE_LOCATION, # "../app/storage"
    "LIB-DIRECTORY": LIBRARIES_LOCATION, # "../app/lib"
    "LOG-DIRECTORY": LOGS_LOCATION, # "../app/log"

    # storage keys
    "XML-MANAGER-TYPE-STORAGE-RECORD": "XML_TYPE_DATA",
    "XML-MANAGER-APP-STORAGE-RECORD": "XML_APPLICATION_DATA",
    "VIRTUAL-HOSTING-STORAGE-RECORD": "VIRTUAL_HOSTING_DATA",
    "FILE-MANAGER-INDEX-STORAGE-RECORD": "STORAGE_FILE_INDEX",
    "RESOURCE-MANAGER-INDEX-STORAGE-RECORD": "RESOURCE_FILE_INDEX",
    "DATABASE-MANAGER-INDEX-STORAGE-RECORD": "DATABASE_FILE_INDEX",
    "SCHEDULER-MANAGER-INDEX-STORAGE-RECORD": "SCHEDULER_INDEX",
    "BACKUP-STORAGE-DRIVER-INDEX-RECORD": "STORAGE_DRIVER_INDEX",
    "SOURCE-SWAP-FILE-INDEX-STORAGE-RECORD": "SWAP_FILE_INDEX",
    "USER-MANAGER-STORAGE-RECORD": "USER_INFO_DATA",
    "USER-MANAGER-ROOT-ID-STORAGE-RECORD": "ROOT_USER_ID",
    "USER-MANAGER-GUEST-ID-STORAGE-RECORD": "GUEST_USER_ID",
    "ACL-MANAGER-STORAGE-RECORD": "ACL_ARRAY_DATA",
    "BACKUP-STORAGE-RECORD": "BACKUP_CONFIG_DATA",
    "VDOM-CONFIG-1-RECORD": "CONFIG_1_DATA",

    # vscript
    "DISABLE-VSCRIPT": DISABLE_VSCRIPT
}

VDOM_CONFIG_1 = {
    "DEBUG": "1",
    "DEBUG-ENABLE-TAGS": "0",
    "ENABLE-PAGE-DEBUG": "0",

    # email settings
    "SMTP-SENDMAIL-TIMEOUT": SMTP_SENDMAIL_TIMEOUT, # 20.0
    "SMTP-SERVER-ADDRESS": SMTP_SERVER_ADDRESS, # ""
    "SMTP-SERVER-PORT": SMTP_SERVER_PORT, # 25
    "SMTP-SERVER-USER": SMTP_SERVER_USER, # ""
    "SMTP-SERVER-PASSWORD": SMTP_SERVER_PASSWORD, # ""

    # security
    "ROOT-PASSWORD": "root"
}
