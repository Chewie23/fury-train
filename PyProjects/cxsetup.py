import sys
from cx_Freeze import setup, Executable

buildOptions = dict(packages = ['jira', 'ConfigParser'], excludes = []) #need to tell cx_freeze which weird package to include!

setup(  name = "ticket",
        version = "0.1",
        description = "My JIRA script",
        options = dict(build_exe = buildOptions),
        executables = [Executable("ticket.py", base = 'Console')])