# Invoke - Pythonic task execution

from os import path
from invoke import task

# .ui files
UI_FILE: list[dict] = [
    {"src": r"ui/mainwindow.ui", "dest": r"ui/ui_mainwindow.py"},
]

# .qrc files
RESOURCES_FILE: list[dict] = [
    {"src": r"ui/resources.qrc", "dest": r"resources_rc.py"},
]

# build all
@task(name="build-all")
def build_all(ctx):
    build_ui(ctx)
    build_resource(ctx)


# .ui files building
@task(name="build-ui")
def build_ui(ctx):
    for each in UI_FILE:
        src: str = path.normpath(each["src"])
        dest: str = path.normpath(each["dest"])
        command: str = f"pyside2-uic {src} -o {dest}"
        ctx.run(command)


# .qrc files building
@task(name="build-resource")
def build_resource(ctx):
    for each in RESOURCES_FILE:
        src: str = path.normpath(each["src"])
        dest: str = path.normpath(each["dest"])
        command: str = f"pyside2-rcc {src} -o {dest}"
        ctx.run(command)
