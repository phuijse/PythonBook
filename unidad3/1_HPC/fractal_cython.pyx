import cython
cimport numpy as npc
import numpy as np

ctypedef npc.float64_t TIPOF_t
ctypedef npc.int64_t TIPOI_t

# Las funciones con cdef solo pueden ser llamadas desde Cython
cdef TIPOI_t evaluate_z(TIPOF_t zi, TIPOF_t zr, int maxiters=50, TIPOF_t cr=-0.835, TIPOF_t ci=-0.2321):
    cdef:
        TIPOI_t nit = 0
        TIPOF_t zi2 = zi**2
        TIPOF_t zr2 = zr**2
        
    while zi2 + zr2 <= 4. and nit < maxiters:
        zi = 2.*zr*zi + ci
        zr = zr2 - zi2 + cr
        zr2 = zr**2
        zi2 = zi**2 
        nit +=1
    return nit

# Las funciones con def pueden ser llamadas desde Python
@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
def make_fractal_cython(int N, TIPOI_t [:, ::1] image_view, int maxiters=50):
    cdef:
        Py_ssize_t i, j
    # Los ndarray no se copian, los podemos modificar inplace desde Cython
    for i in range(N):
        for j in range(2*N):
            image_view[i, j] = evaluate_z(-1.+i*2./N, -2.+j*2./N, maxiters)