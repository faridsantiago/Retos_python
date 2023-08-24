
diccionario_productos = {
    1: "Nike Air Max 90",
    2: "Jeans h&m",
    3: "Bolso de cuero"
}

diccionario_categorias = {
    1: "Zapatos",
    2: "Prendas de vestir",
    3: "Accesorios"
}

# Crear el diccionario resultante utilizando diccionarios por comprensión
diccionario_resultante = {
    producto_nombre: diccionario_categorias.get(producto_id)
    for producto_id, producto_nombre in diccionario_productos.items()
}

print(diccionario_resultante)



