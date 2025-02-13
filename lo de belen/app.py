from conexion_firebase import obtener_ropa, agregar_prenda

ropa = obtener_ropa()
for prenda in ropa:
    print(prenda)


agregar_prenda("Zapatos Del Dragon", "calzado", "42", "negros", 49.99, 10)
