def funcion_interesante(n):
    """
    Este script es interesante
    """
    if n == 1:
        return 1

    else:
        return n * funcion_interesante(n-1)

if __name__ == '__main__':
    print(funcion_interesante(10))
        