# Computación Científica con Python

Un libro virtual diseñado como recurso de aprendizaje para los estudiantes del curso de Computación Científica con Python (INFO147) de la carrera de Ingeniería Civil en Informática de la Universidad Austral de Chile. El libro fue escrito por Pablo Huijse y está en continuo desarrollo.

El código fuente del libro está en https://github.com/phuijse/PythonBook. El libro virtual está publicado en : https://phuijse.github.io/PythonBook/. El libro fue desarrollado utilizando [`jupyter-book`](https://jupyterbook.org/intro.html). Si encuentras errores por favor deja un *issue* en el repositorio que contiene el libro.

**Contenidos**

- Exploración interactiva de datos con `Ipython` y `Jupyter`
- Manejo de datos con `pandas`
- Visualización de datos con `matplotlib`
- Álgebra lineal con `numpy`
- Optimización numérica con `scipy`
- Estadística descriptiva e inferencial con `scipy`
- Introducción a Machine Learning con `scikit-learn`
- Optimización de cómputo con `cython`

**Referencias**

1. [Jake VanderPlas, "Python Data Science Handbook", *O'Reilly*, 2016](https://jakevdp.github.io/PythonDataScienceHandbook/)
1. [Cyrille Rossant, "IPython Cookbook", 2ed, *Packt*, 2018](https://ipython-books.github.io/)
1. [Robert Johansson, "Numerical Python", 2ed, *Apress*, 2018](https://link.springer.com/book/10.1007%2F978-1-4842-4246-9)
1. [K. Reith y T. Schulesser, "The Hitchhiker's guide to Python", *O'Reilly*, 2016](https://docs.python-guide.org)
1. [J. VanderPlas, "Whirlwind Tour of Python", *O'Reilly*, 2016](https://github.com/jakevdp/WhirlwindTourOfPython)
1. [C.H. Swaroop, "A Byte of Python", 2015](https://python.swaroopch.com)
1. [Brett Slakin, "Effective Python", *Addison-Wesley*, 2015](https://effectivepython.com/)
1. [Greg Wilson, et al., "Best Practices for Scientific Computing", PLOS Biology, 2014](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001745)
1. [Adam Rule, et al. "Ten simple rules for writing and sharing computational analyses in Jupyter Notebook", PLOS Computational Biology, 2019](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1007007)

**Como compilar este libro**

1. Clonar el repositorio: `git clone https://github.com/phuijse/PythonBook.git`
1. Instalar dependencias: `pip install -r requirements.txt`
1. Ejecutar los cuadernillos
1. Compilar libro: `jupyter-book build .`
1. (Opcional) Subir a github pages:  `ghp-import -n -p -f _build/html/`
