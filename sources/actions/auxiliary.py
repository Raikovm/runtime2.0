
from contextlib import contextmanager
from textwrap import wrap
from logs import console
from utils.structure import Structure
from utils.auxiliary import align


MISSING = "MISSING"
INDENT = "    "

NAME_WIDTH = 36
LONG_NAME_WIDTH = NAME_WIDTH * 2
VALUE_WIDTH = 68


global_indent = ""
global_section = None


def escape(value):
    return "\"%s\"" % value.replace("\"", "\\\"")


@contextmanager
def section(name=None, value=MISSING, instant=False):
    global global_indent, global_section

    indent = global_indent
    context = Structure(global_section=global_section)

    def show_section():
        global global_section
        if context.global_section:
            context.global_section()
            context.global_section = None
        global_section = None
        show(name, value, indent=indent)

    if value is MISSING and not instant:
        global_section = show_section
    else:
        show_section()
        global_section = None

    global_indent += INDENT
    yield
    global_indent = global_indent[:-len(INDENT)]
    global_section = context.global_section


def show(name=None, value=MISSING, indent=None, longer=False):
    global global_indent, global_section

    if global_section is not None:
        global_section()
        global_section = None

    if indent is None:
        indent = global_indent

    if value is MISSING:
        value = name
        caption = indent
    else:
        if not isinstance(value, basestring):
            value = str(value)

        name_width = LONG_NAME_WIDTH if longer else NAME_WIDTH
        filler = "." if name else " "
        caption = align(name, name_width, filler=filler, indent=indent)

    message = "\n".join(("\n".join(
        wrap(part,
            initial_indent=caption,
            subsequent_indent=" " * len(caption),
            width=NAME_WIDTH + VALUE_WIDTH,
            replace_whitespace=False,
            break_long_words=False)) for part in value.splitlines()))
    console.write(message)


def confirm(message):
    console.write(message)
    console.stdout.write("are you sure? ")
    answer = raw_input()
    return answer.lower() == "yes"
