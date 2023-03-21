# ¿Qué es Jupyter?


[Jupyter](https://jupyter.org/) es un proyecto que incorpora:

- El formato `notebook`
- Un servidor web para editar y visualizar `notebooks`
- Un protocolo de mensajería para comunicar el `notebook` con un `kernel` 

El `kernel` recibe código y retorna los resultados al `notebook`. En general trabajaremos con [IPython](https://ipython.org/), el intérprete de Python interactivo, como kernel.

El `notebook` es un formato relativamente nuevo que combina:

- código 
- visualizaciones 
- ecuaciones
- texto enriquecido
- imágenes, audio, video
- interfaces de usuario (GUI)
- entre otros

esto lo hace ideal para 

- explorar y analizar datos de forma interactiva
- comunicar y compartir resultados
- crear "[narrativas científicas](https://github.com/mcburton/computational-narratives-with-jupyter)" interactivas


**Ejemplos**

Revisa uno o más de los siguientes ejemplos para hacerte una idea de lo que se puede hacer con Jupyter

- Visualización de datos de censo (Estados Unidos): https://anaconda.org/jbednar/census/notebook
- Jupyter notebook sobre reacciones químicas: https://nbviewer.jupyter.org/gist/greglandrum/4316430
- Un tutorial de GIT escrito en jupyter: https://nbviewer.jupyter.org/github/fperez/reprosw/blob/master/Version%20Control.ipynb
- Este libro fue creado en base a jupyter notebooks

## Qué no es Jupyter

Jupyter no es un reemplazo para una IDE completa como [*pycharm*](https://www.jetbrains.com/pycharm/) o [*vscode*](https://code.visualstudio.com/) ni editores como [*vim*](https://www.vim.org/) o [*emacs*](https://www.gnu.org/software/emacs/). Jupyter es un complemento.

No es directo ni sencillo reutilizar (importar) código que está en jupyter notebook. Por razones como esta los notebooks no suelen ser usados para tareas de producción.

Si tu notebook tiene rutinas que pueden ser utilizadas por otros notebooks o scripts lo mejor es escribir la rutina como un módulo regular de Python y luego importarlo desde el notebook.

:::{hint}

Usando la magia `%autoreload 2` puedes hacer cambios "en vivo" en los módulos importados por el notebook sin tener que reiniciarlo.

:::

Revisa la siguiente presentación sobre [Buenas prácticas con Jupyter notebook](https://docs.google.com/presentation/d/1TKOjhFsYM4R_iIhMGPuS5h3fY_AxHpzxPQ3MKVwmzOc/edit#slide=id.g872e56ba64_0_0) para más consejos.


## ¿Cómo funciona Jupyter?

La siguiente figura muestra los componentes del ambiente jupyter.

<img src="img/notebook_components.png" width="600">

- El **servidor jupyter** es el encargado de administrar los `notebooks`.
- Los usuarios interactuan con los `notebooks` a través de su navegador (*frontend* web) o IDE.
- El proceso encargado de correr los códigos se denomina `kernel`.
- El servidor conecta los notebooks con el kernel usando la librería de mensajería ZeroMQ.


**¿Qué lenguajes puedo usar con Jupyter?**

Existen `kernels` de Python, Julia, Ruby, C y otros lenguajes. En este libro nos enfocaremos en el kernel *Interactive Python* o  IPython.

IPython es un interprete de Python que ofrece varias mejoras tales como:

- autocompletación de path y módulos
- acceso desde terminal a documentación y código fuente
- búsqueda histórica de comandos
- instrucciones especiales llamadas *magics* que serán vistas más adelante


:::{note}

IPython reemplaza al intérprete convencional de Python. No necesitamos Jupyter para utilizar IPython, simplemente escribe `ipython` en un terminal.

:::

:::{note}

Además del frontend por defecto existe [jupyter lab](https://jupyter.org/). Este último tiene una interfaz de usuario más similar al de una IDE completa.

:::

## Creando un ambiente para cómputo interactivo con jupyter

Utilizando conda creamos un ambiente con Python 3.10 (o superior) con las librerías necesarias:

    conda create -n info147 python=3.10 pip jupyter numpy matplotlib pandas scipy ipympl
    
Luego activamos el ambiente:

    conda activate info147
    
Finalmente iniciamos el servidor jupyter escribiendo en la terminal:

    jupyter notebook
    
Esto abrirá una pestaña de navegador (browser) apuntada en la dirección:

    http://localhost:8888



