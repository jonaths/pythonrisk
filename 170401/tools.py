import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi

class Tools:

    @staticmethod
    def getArrayMinMax(array):
        """Maximo y minimo de array
        
        Regresa un vector con los maximos y minimos por cada dimension del 
        vector de entrada. 
        
        Arguments:
            array {array} -- Un arreglo de n filas por m columnas
                                Cada fila es una muestra
                                Cada columna representa una dimension
        
        Returns:
            array -- un arreglo [[max_dim_1,min_dim_1],[max_dim_2,min_dim_2... ]]
        """
        matrix = np.array(array)
        num_elements,vec_dimension = matrix.shape
        maxmin = []
        for c in range( 0,vec_dimension ):
            min = np.min( matrix[:, c] )
            max = np.max( matrix[:, c] )
            maxmin.append([max,min])

        return maxmin

        