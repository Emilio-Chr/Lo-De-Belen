import firebase_admin
from firebase_admin import credentials, firestore

# Cargar credenciales y conectar Firebase
cred = credentials.Certificate("prueba-e56b3-firebase-adminsdk-fbsvc-ec550799fb.json")  # 🔹 Cambia la ruta
firebase_admin.initialize_app(cred)

# Crear instancia de Firestore
db = firestore.client()

# Función para obtener toda la ropa de Firestore
def obtener_ropa():
    ropa_ref = db.collection("ropa")
    docs = ropa_ref.stream()
    return [doc.to_dict() for doc in docs]

# Función para agregar una prenda
def agregar_prenda(nombre, categoria, talla, color, precio, stock):
    db.collection("ropa").add({
        "nombre": nombre,
        "categoria": categoria,
        "talla": talla,
        "color": color,
        "precio": precio,
        "stock": stock
    })
    print("Prenda añadida correctamente.")


