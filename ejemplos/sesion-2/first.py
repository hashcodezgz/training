"""Primera sesion.

Este es un análisis de humansize.py basado en
http://www.diveintopython3.net/your-first-python-program.html

"""

""" humansize.py:
# $ python3 humansize.py
# 1.0 TB
# 931.3 GiB
"""

""" import:

¿Dónde python busca el código?
¿Dónde ipython busca el código?
¿Cómo se importa código?
"""

import sys
sys.path.insert(0, "/Users/javier/git/hashcode-training/ejemplos/sesion-2")
from humansize import approximate_size
approximate_size(1000000000000)

""" definición de una función:

def approximate_size(size, a_kilobyte_is_1024_bytes=True):
    pass
"""

approximate_size(4000, False)
approximate_size(4000, a_kilobyte_is_1024_bytes=False)
approximate_size(size=4000, a_kilobyte_is_1024_bytes=False)
approximate_size(a_kilobyte_is_1024_bytes=False, size=4000)
# approximate_size(a_kilobyte_is_1024_bytes=False, 4000)
# approximate_size(size=4000, False)

""" docstrings:

"""
print(approximate_size.__doc__)
print(sys.__doc__)

""" algunas ideas clave:
- identación: funciones, for, if, ...
- for, if
- declaración automática de variables
- if como expresión
- todo es un objeto
- excepciones/try/raise/except

"""
from humansize import SUFFIXES


def approximate_size2(size, a_kilobyte_is_1024_bytes=True):
    """Esta función es de ejemplo."""
    if size < 0:
        raise ValueError('number must be non-negative')

    multiple = 1024 if a_kilobyte_is_1024_bytes else 1000
    for suffix in SUFFIXES[multiple]:
        size /= multiple
        if size < multiple:
            return '{0:.1f} {1}'.format(size, suffix)

    raise ValueError('number too large')


approximate_size(-1)

try:
    approximate_size(-1)
except ValueError:
    print("Se ha producido un error")

try:
    from lxml import etree
except ImportError:
    import xml.etree.ElementTree as etree

help(etree.Error.__cause__)

""" ejecución de scripts:
if __name__ == '__main__':
    print(approximate_size(1000000000000, False))
    print(approximate_size(1000000000000))
"""
import humansize
print(humansize.__name__)
