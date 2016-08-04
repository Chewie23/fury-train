import sys
from cx_Freeze import setup, Executable

buildOptions = dict(packages = ['random'], excludes = [])

setup(  name = "coin_or_die",
        version = "0.1",
        description = "My coin or die simulation",
        options = dict(build_exe = buildOptions),
        executables = [Executable("DieRolling.py", base = 'Console')])