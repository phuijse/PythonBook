# Fractal de Mandelbrot

x = np.linspace(-2, 1, num=2000)
y = np.linspace(-1.5, 1.5, num=2000)
X, Y = np.meshgrid(x, y)
C = X + 1j*Y
Z = np.zeros_like(C)

for i in range(1000):
    Z = Z*Z + C

FRACTAL = np.isnan(Z)
