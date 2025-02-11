
from .auxiliary.constants import TYPES, APPLICATIONS
from .auxiliary import section, warn, select


ENTITIES = TYPES, APPLICATIONS


def run(identifier, yes=False):
    """
    uninstall application or type
    :arg uuid_or_name identifier: application or type uuid or name or types to uninstall all types
    :key switch yes: assume positive answer to confirmation request
    """
    for entity, subject in select(identifier, "uninstall", ENTITIES, confirm=not yes):
        with section("uninstall %s" % subject, lazy=False):
            try:
                subject.uninstall()
            except Exception as error:
                warn("unable to uninstall %s: %s" % (entity, error))
                raise
