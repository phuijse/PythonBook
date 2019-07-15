def make_fractal(N, maxiter=50):
    image = []
    cr, ci = -0.835, -0.2321
    # cr, ci = -0.1, 0.65
    def initialize(i, j):
        zi = -1.0 + i*2/N
        zr = -2.0 + j*2/N
        return zi, zr
    
    def evaluate(zi, zr):
        nit = 0
        zi2 = zi*zi
        zr2 = zr*zr
        while zi2 + zr2 <= 4. and nit < maxiter:
            zi = 2*zr*zi + ci
            zr = zr2 - zi2 + cr
            zr2 = zr*zr
            zi2 = zi*zi 
            nit +=1
        return nit
    
    for i in range(N):
        row = []
        for j in range(2*N):
            zi, zr = initialize(i, j)
            row.append(evaluate(zi, zr)/maxiter)
        image.append(row)
    return image