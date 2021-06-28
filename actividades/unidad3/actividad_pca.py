#%%
%matplotlib ipympl
import matplotlib.pyplot as plt
import sklearn.datasets

# Descargar la data, esto demora un poco
lfw_people = sklearn.datasets.fetch_lfw_people(min_faces_per_person=20, resize=0.4)
X = lfw_people['data'].astype('float64')
display(X.shape)

# Visualizando los 21 primeros ejemplos
fig, ax = plt.subplots(3, 7, figsize=(7, 4), tight_layout=True)
for i, ax_ in enumerate(ax.ravel()):
    ax_.axis('off')
    ax_.imshow(X[i, :].reshape(50, 37), cmap=plt.cm.Greys_r);

# Este subset del dataset Labeled Faces in the Wild (LFW) tiene 3023 imágenes de rostros en blanco y negro y de 37x50 píxeles. 
# En esta actividad interpretaremos este dataset como una matriz de 3023 filas (ejemplos) y 1850 atributos (píxeles)
#  Más detalles del dataset aquí: https://scikit-learn.org/stable/datasets/real_world.html#the-labeled-faces-in-the-wild-face-recognition-dataset
  
# Para realizar esta actividad se recomienda haber revisado previamente la sección sobre PCA (3.1) de la lección https://magister-informatica-uach.github.io/INFO147/clases/unidad3/1_ML/ML3.html

# Instrucciones
# Utilice sklearn.decomposition.PCA para encontrar los "rostros principales" (vectores propios) del dataset LFW. Muestre los 21 rostros principales de mayor varianza. HINT: Atributo components_ de PCA
# Cree una interfaz interactiva (ipywidgets) que muestre la reconstrucción de los 21 primeros ejemplos en función de la "varianza total acumulada". HINT: revisar opción float del argumento n_components del constructor de PCA y el método inverse_transform

#%%
