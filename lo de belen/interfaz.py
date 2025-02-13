import tkinter as tk
from tkinter import messagebox
import firebase_admin
from firebase_admin import credentials, firestore

# Cargar credenciales y conectar Firebase
cred = credentials.Certificate("prueba-e56b3-firebase-adminsdk-fbsvc-ec550799fb.json")  
firebase_admin.initialize_app(cred)

db = firestore.client()

class CRUDApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CRUD de Ropa")
        self.root.configure(bg="#f4f4f4")
        
        # Frame para organizar los elementos
        frame = tk.Frame(root, padx=20, pady=20, bg="#ffffff", relief="groove", borderwidth=3)
        frame.pack(padx=20, pady=20)

        labels = ["ID:", "Nombre:", "Categoría:", "Talla:", "Color:", "Precio:", "Stock:"]
        self.entries = {}
        
        for i, label_text in enumerate(labels):
            label = tk.Label(frame, text=label_text, font=("Arial", 12), bg="#ffffff")
            label.grid(row=i, column=0, sticky="w", pady=5)
            entry = tk.Entry(frame, font=("Arial", 12), width=30, relief="solid", borderwidth=2)
            entry.grid(row=i, column=1, pady=5)
            self.entries[label_text] = entry
        
        # Frame para los botones
        button_frame = tk.Frame(root, bg="#f4f4f4")
        button_frame.pack(pady=10)

        button_style = {"font": ("Arial", 12, "bold"), "width": 15, "pady": 5, "borderwidth": 3}

        self.add_button = tk.Button(button_frame, text="Agregar", command=self.add, bg="#4CAF50", fg="white", **button_style)
        self.add_button.grid(row=0, column=0, padx=5, pady=5)

        self.read_button = tk.Button(button_frame, text="Leer", command=self.read, bg="#2196F3", fg="white", **button_style)
        self.read_button.grid(row=0, column=1, padx=5, pady=5)

        self.update_button = tk.Button(button_frame, text="Actualizar", command=self.update, bg="#FFC107", fg="black", **button_style)
        self.update_button.grid(row=1, column=0, padx=5, pady=5)

        self.delete_button = tk.Button(button_frame, text="Eliminar", command=self.delete, bg="#F44336", fg="white", **button_style)
        self.delete_button.grid(row=1, column=1, padx=5, pady=5)
    
    def add(self):
        data = {key[:-1].lower(): entry.get() for key, entry in self.entries.items() if key != "ID:"}
        if all(data.values()):
            db.collection("ropa").add(data)
            messagebox.showinfo("Éxito", "Prenda añadida correctamente")
        else:
            messagebox.showerror("Error", "Todos los campos excepto ID son obligatorios")
    
    def read(self):
        doc_id = self.entries["ID:"].get()
        if doc_id:
            doc = db.collection("ropa").document(doc_id).get()
            if doc.exists:
                data = doc.to_dict()
                for key, entry in self.entries.items():
                    field = key[:-1].lower()
                    if field in data:
                        entry.delete(0, tk.END)
                        entry.insert(0, str(data[field]))
                messagebox.showinfo("Éxito", "Datos cargados correctamente")
            else:
                messagebox.showerror("Error", "No se encontró la prenda con ese ID")
        else:
            messagebox.showerror("Error", "El campo ID es obligatorio")
    
    def update(self):
        doc_id = self.entries["ID:"].get()
        if doc_id:
            doc_ref = db.collection("ropa").document(doc_id)
            doc = doc_ref.get()
            if doc.exists:
                data = {key[:-1].lower(): entry.get() for key, entry in self.entries.items() if key != "ID:"}
                if all(data.values()):
                    doc_ref.update(data)
                    messagebox.showinfo("Éxito", "Prenda actualizada correctamente")
                else:
                    messagebox.showerror("Error", "Todos los campos deben estar llenos para actualizar")
            else:
                messagebox.showerror("Error", "No se encontró la prenda con ese ID")
        else:
            messagebox.showerror("Error", "El campo ID es obligatorio")
    
    def delete(self):
        doc_id = self.entries["ID:"].get()
        if doc_id:
            doc_ref = db.collection("ropa").document(doc_id)
            doc = doc_ref.get()
            if doc.exists:
                doc_ref.delete()
                messagebox.showinfo("Éxito", "Prenda eliminada correctamente")
            else:
                messagebox.showerror("Error", "No se encontró la prenda con ese ID")
        else:
            messagebox.showerror("Error", "El campo ID es obligatorio")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x450")  # Ajustar tamaño
    app = CRUDApp(root)
    root.mainloop()
