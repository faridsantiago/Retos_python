import math

lista_coordenadas= [(1,2),(3,4),(5,6),(7,8),(3,9)]

#calculamos la distancia minima utilizando una formula que encontré en google
def distancia(p1,p2):
    return math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)

#funcion que calcula los pares mas cercanos
def pares_cercanos_util(puntos):
    n = len(puntos)

    #si hay pocos puntos, realzia todas las combinaciones y devolvemos la minima
    if n <= 3:
        minimo = float('inf')
        for i in range(n):
            for j in range(i+1,n):
                dist = distancia(puntos[i],puntos[j])

                if dist < minimo:
                    minimo = dist
                    close_pair = (puntos[i],puntos[j])
        return minimo, close_pair
    
    #Divide el conjunto de puntos en dos mitades
    mid = n//2
    mid_point = puntos[mid]

    left_points = puntos[:mid]
    right_points = puntos[mid:]

    #Encuentra los par mas cercano en cada mitad
    left_min_dist, left_pair = pares_cercanos_util(left_points)
    right_min_dist, right_pair = pares_cercanos_util(right_points)

    #encuentra la distancia minima entre las mitades izquierda y derecha
    if left_min_dist < right_min_dist:
        minimo = left_min_dist
        close_pair = left_pair
    else:
        minimo = right_min_dist
        close_pair = right_pair 
    
    # Crea una franja de puntos que están cerca de la línea vertical
    strip = []
    for point in puntos:
        if abs(point[0]-mid_point[0]) < minimo:
            strip.append(point)
        
        strip.sort(key = lambda point: point[1])
        
        # Comprueba las distancias en la franja y actualiza si es necesario
        for i in range(len(strip)):
            j = i+1

            while j < len(strip) and (strip[j][1]-strip[i][1]) < minimo:
                dist = distancia(strip[i],strip[j])
                if dist < minimo:
                    minimo = dist
                    close_pair = (strip[i],strip[j])
                j += 1
    return minimo, close_pair

# Función principal que acepta argumentos individuales
def pares_cercanos(**kwargs):
    puntos = kwargs.get('puntos',[])
    puntos.sort()
    return pares_cercanos_util(puntos)

minimo, close_pair = pares_cercanos(puntos=lista_coordenadas)
print("La distancia minima es: ",minimo)
print("Los puntos mas cercanos son: ",close_pair)
