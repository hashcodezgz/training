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

Para instalar paquetes de python la manera más sencilla es usar pip:
```
pip install pylint pep8 flake8 jedi
```
Si no teneis instalado pip unicamente tenéis que descargaros el archivo:
[get_pip.py](https://bootstrap.pypa.io/get-pip.py)

abrir una terminal en la carpeta donde se encuentre el archivo y ejecutar_
```
python get-pip.py
```
## Configuración de ATOM

Después en *ATOM* tenemos que ir a **"Preferences..."**.

En preferencias de **"Editor"** activamos:
*   **“Show Indent Guide”** para mostrar guías de sangrado.
*   **“Show Invisibles"** para mostrar caracteres ocultos.

En **"File->Settings->Install"** instalamos los siguientes paquetes y sus dependencias:
*   [linter-pylint](https://atom.io/packages/linter-pylint) que utiliza *pylint* para revisar el código.
*   [linter-flake8](https://atom.io/packages/linter-flake8) que utiliza *flake8* para revisar el código.
*   [linter-python-pep8](https://atom.io/packages/linter-python-pep8) que utiliza *pep8*.
*   [autocomplete-python](https://atom.io/packages/autocomplete-python) que te da a elegir entre *jedi* y [Kite](https://kite.com/), un servicio de cloud de autocompletado.
*
En el caso de linux, se pueden instalar paquetes de *ATOM* con
```
apm install packagename
```

## Hydrogen
Hydrogen es un paquete que permite ejecutar código utilizando los kernels de jupyter

Una vez en *ATOM* **File->Settings->Install** instalamos el paquete de [Hydrogen](https://atom.io/packages/Hydrogen)

Guía completa de uso de Hydrogen --><https://nteract.gitbooks.io/hydrogen/docs/Usage/GettingStarted.html>

Para poder ejecutar un código será necesario instalar los [kernels](https://github.com/jupyter/jupyter/wiki/Jupyter-kernels) correspondientes

En el caso de python3 su kernel es [ipykernel](https://github.com/ipython/ipykernel)
```
python -m pip install ipykernel
python -m ipykernel install --user

```
### Ejecucción
Para ejecutar una linea de código pulsamos **ctr+enter o shift+enter**

Tambien podemos declarar celdas al estilo de Jupyter
```
print("Celda 1")

# %%
print("Celda 2")
print("Sigue siendo celda 2")

# <codecell>
print("Celda 3")

# In[]
print("Celda 4")

# In[1]
print("Celda 5")

```
Se puede ejecutar una celda entera pulsando **alt+ctr+enter o alt+shift+enter**

Para ejecutar todo el código pulsamos **alt+ctr+shift+enter**
### Watch expression
Una de las características mas llamativas es el uso del *Watch Expression*

Para usarlo hay que abrir el panel de expresiones pulsando **ctr+shift+p** y
seleccionando la opción de **toggle watches**.

Una vez abierto el panel de expresiones, podemos introducir una variable, expresión...
y al ejecutar el kernel nos mostrará su valor. Cada vez que cambiemos el código y
volvamos a ejecutar, se volverá a calcular su valor.

Por ejemplo si en este código vigilamos la variable `x`
```
x = 2 + 2

```
El valor que nos mostrará es 4
Si cambiamos el código y ejecutamos de nuevo
```
x = 2 + 6

```
El valor de la variable ahora será 6

Es muy útil para comprobar resultados de variables en celdas muy grandes.
También es capaz de enseñar gráficos y tablas.

### Code instropection
Abriendo la paleta de Atom **ctr+shift+p** y seleccionado **Toggle Inspector** se abrirá
una ventana con información de la función que estemos señalando, sus parámetros y como ejecutarla.

### Restablecer kernels
Es posible interrumpir apagar o restablecer kernels para empezar una nueva ejecución
pulsando sobre el nombre del kernel que estáis usando en la parte inferior izquierda de ATOM

## Teletype
Teletype es una potente herramienta que permite un trabajo concurrente sobre un mismo documento
al estilo de Google Docs.

Para usarlo es necesario instalar su paquete [teletype](https://github.com/atom/teletype)

Una vez instalado aparecerá en la parte inferior derecha un icono de una antena.
Os pedirá que inicies sesión en [Github](https://github.com/), una vez iniciada,
aparecerá un token que deberéis pegar en la pestaña de teletype.

Una vez logeados ya se puede empezar a colaborar, para compartir un proyecto únicamente
es necesario activar el share y compartir el token_ID de proyecto.

Para unirse a un proyecto, presionar en **join a portal** e introducir el token_ID proporcionado

## Git
Atom incorpora la herramienta git, para abrir el panel únicamente presionar
**ctr+shift+9 o Packages->Github->Toggle git tab**

Si tu proyecto se encuentra en un repositorio git local, en la pestaña aparecerán
los ficheros donde se han realizado cambios.

Para guardar los cambios, primero haremos un *stage* de los ficheros que queramos cambiar,
escribiremos un mensaje de *commit* y
realizaremos después el *commit*.

Para enviar los cambios a GitHub, pulsaremos en el icono de las dos flechas
de la parte inferior derecha y pulsaremos **push**.
Para recibir cambios que otros han subido a la nube pulsaremos el botón **pull**

Podemos encontrar documentación en <http://blog.atom.io/2014/03/13/git-integration.html>
