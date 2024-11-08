import pyrebase
from config import get_firebase_config

class Database:
    def __init__(self):
        config = get_firebase_config()
        firebase = pyrebase.initialize_app(config)
        self.db = firebase.database()

    def login_user(self, username, password):
        # Mendapatkan data login dari Firebase
        users = self.db.child("login").get()
        
        for user in users.each():
            data = user.val()
            # Cocokkan username dan password
            if data.get("username") == username and data.get("password") == password:
                return True
        return False

    def simpan_data(self, username, nama, ibu, umur, telepon):
        # Simpan data balita dengan ID unik
        data = {
            "ibu": ibu,
            "nama": nama,
            "telepon": telepon,
            "umur": umur,
        }
        # Simpan ke Firebase dengan ID unik untuk setiap entri
        self.db.child("balita").child(username).push(data)  # Menggunakan push untuk menambahkan entri baru

    def ambil_data(self, username):
        # Inisialisasi list untuk menyimpan data balita
        data_balita = []
        
        try:
            # Mengambil data balita dari Firebase di bawah node 'balita/username'
            balita_data = self.db.child("balita").child(username).get()
            
            # Periksa apakah ada data
            if balita_data.each() is not None:
                # Loop melalui setiap entri data balita
                for balita in balita_data.each():
                    # Tambahkan data balita ke dalam list
                    data_balita.append(balita.val())
            else:
                print("Tidak ada data untuk username ini.")
                
        except Exception as e:
            print(f"Error saat mengambil data dari Firebase: {e}")

        # Kembalikan list data balita
        return data_balita

