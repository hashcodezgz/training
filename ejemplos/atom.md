# Cómo configurar ATOM como tu entorno ligero de desarrollo Python

## Configuración de Python

Aseguramos que están instalados los siguientes paquetes de Python:
*   [pylint](https://www.pylint.org/) uno de los analizadores más potentes.
*   [pep8](https://pypi.python.org/pypi/pep8)
es una herramienta que verifica si el código sigue las convenciones de estilo de
[PEP 8](https://www.python.org/dev/peps/pep-0008/).
*   [flake8](https://pypi.python.org/pypi/flake8) es un wrapper alrededor de
[PyFlakes](https://pypi.python.org/pypi/pyflakes),
[pycodestyle](https://pypi.python.org/pypi/pycodestyle) y
[McCabe](https://pypi.python.org/pypi/mccabe),
todas ellas herramientas de chequeo de calidad de código
(estilo, errores potenciales, complejidad).
*   [jedi](https://pypi.python.org/pypi/jedi)
es una herramienta de autocompletado para Python.

Para instalarlos solo tenemos que ejecutar:
```
pip install pylint pep8 flake8 jedi
```

## Configuración de ATOM

Después en *ATOM* tenemos que ir a **"Preferences..."**.

En preferencias de **"Editor"** activamos:
*   **“Show Indent Guide”** para mostrar guías de sangrado.
*   **“Show Invisibles"** para mostrar caracteres ocultos.

En **"Install"** instalamos los siguientes paquetes y sus dependencias:
*   [linter-pylint](https://atom.io/packages/linter-pylint) que utiliza *pylint* para revisar el código.
*   [linter-flake8](https://atom.io/packages/linter-flake8) que utiliza *flake8* para revisar el código.
*   [linter-python-pep8](https://atom.io/packages/linter-python-pep8) que utiliza *pep8*.
*   [autocomplete-python](https://atom.io/packages/autocomplete-python) que te da a elegir entre *jedi* y [Kite](https://kite.com/), un servicio de cloud de autocompletado.
