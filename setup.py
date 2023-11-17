import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

executables = [
    Executable('oi rs.py', base=base)
]

setup(name='Pedido de namoro',
    version= '1',
    description= 'App que pede em namoro sem possibilidade de não',
    executables= executables
)