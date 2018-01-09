# Traslados
_Jorge Pinilla López_

_09/01/2018_

Tenemos unas solicitudes de traslado entre carreras:

| Carreras \ Traslados | Informatica | Derecho | Magisterio |
| -------------------- | ----------- | ------- | ---------- |
| Informatica          | ---         | 5       | 2          |
| Derecho              | 1           | ---     | 6          |
| Magisterio           | 1           | 3       | ---        |

Esta tabla indica que por ejemplo un alumno de derecho quiere trasladarse a informática.

El objetivo es dar una solución de traslados acceptados teniendo en cuenta:
1. Se quiere maximizar el número de Traslados
2. El numero de personas en cada carrera ha de ser constante--el numero de personas que se trasladan de una carrera tiene que ser igual al numero de personas que vienen a esa carrera (la suma de las columnas de una carrera
tienen que ser igual a la suma de sus filas)

Una solución correcta sería

| Carreras \ Traslados | Informatica | Derecho | Magisterio |
| -------------------- | ----------- | ------- | ---------- |
| Informatica          | ---         | 2       | 0          |
| Derecho              | 1           | ---     | 4          |
| Magisterio           | 1           | 3       | ---        |

El numero de traslados totales sería de 11 y es correcto ya que:

Informatica: 2+0 == 1+1

Derecho: 1+4 == 2+3

Magisterio: 1+3 = 0+4

## Fichero de entrada y salida
El fichero de entrada y salida (csv) se compone de valores separados por , tal que:

- Primera linea con los nombres de las carreras
- En las siguientes lineas, los traslados pedidos por cada carrera
- En los campos donde no se pueda poner información (ejemplo Traslados
de informatica a informatica habrá una x)

ejemplo (example.in.csv):

```
Informatica,Derecho,Magisterio
x,5,2
1,x,6
1,3,x
```
