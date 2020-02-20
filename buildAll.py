# -*- coding: utf-8 -*-


import os
import subprocess
import sys

from ruamel.yaml import YAML
from ruamel.yaml.compat import StringIO


class MyYAML(YAML):

    def dump(self, data, stream=None, **kw):
        inefficient = False
        if stream is None:
            inefficient = True
            stream = StringIO()
        YAML.dump(self, data, stream, **kw)
        if inefficient:
            return stream.getvalue()


def runCommand(command: list):
    proc = subprocess.Popen(command, stderr=subprocess.PIPE)
    out, err = proc.communicate()
    if err:
        msg = err.decode("utf-8")
        print(msg, file=sys.stderr)
    return proc.returncode


def uic(inputFile: str, outputFile: str):
    command: list = ['uic', '-g', 'python', inputFile, '-o', outputFile]
    return runCommand(command)


def rcc(inputFile: str, outputFile: str):
    command: list = ['rcc', '-g', 'python', inputFile, '-o', outputFile]
    return runCommand(command)


def main(verbose: bool = True):
    with open('build.yml', 'r', encoding='utf-8') as file:
        for i in MyYAML().load(file.read()):
            if i['type'] == 'ui':
                try:
                    os.remove(i['pyName'])
                except FileNotFoundError:
                    pass
                uic(i['name'], i['pyName'])
                if verbose is True:
                    print('{0} > {1}'.format(i['name'], i['pyName']))
            elif i['type'] == 'qrc':
                try:
                    os.remove(i['pyName'])
                except FileNotFoundError:
                    pass
                rcc(i['name'], i['pyName'])
                if verbose is True:
                    print('{0} > {1}'.format(i['name'], i['pyName']))


if __name__ == '__main__':
    main()
