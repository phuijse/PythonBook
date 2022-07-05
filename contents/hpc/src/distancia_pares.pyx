import cython
cimport numpy as npc
import numpy as np

# Tipo fusionado
ctypedef fused TIPO_t:
    npc.float32_t
    npc.float64_t # double
    
cdef extern from "math.h":
    npc.float32_t sqrtf(npc.float32_t) #Definición para float32
    npc.float64_t sqrt(npc.float64_t) # Definición para float64

@cython.boundscheck(False)
@cython.wraparound(False)
def distancia_pares_cython_multitipo(TIPO_t [:, ::1] data):
    cdef int N = data.shape[0]
    cdef int M = data.shape[1]
    # Comprobamos el tipo antes de crear el arreglo de numpy
    if TIPO_t is npc.float32_t:
        TIPO = np.float32
    else:
        TIPO = np.float64
    dist = np.zeros(shape=(N, N), dtype=TIPO)
    cdef TIPO_t [:, ::1] dist_view = dist
    cdef Py_ssize_t i, j, k
    for i in range(N):
        for j in range(i+1, N):
            for k in range(M):
                dist_view[i, j] += (data[i, k] - data[j, k])**2
            if TIPO_t is npc.float32_t:
                dist_view[i, j] = sqrtf(dist_view[i, j])
            else:
                dist_view[i, j] = sqrt(dist_view[i, j])
            dist_view[j, i] = dist_view[i, j]
    return dist
