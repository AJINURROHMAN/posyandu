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
                return True  # Login berhasil
        return False  # Login gagal

    def get_user_data(self, username):
        # Mendapatkan data pengguna berdasarkan username
        user_data = self.db.child("login").order_by_child("username").equal_to(username).get()
        if user_data.each():
            return user_data.each()[0].val()  # Mengembalikan data pengguna pertama yang cocok
        return None  # Tidak ada data pengguna ditemukan

    def simpan_data_balita(self, username, nama, ibu, umur, telepon):
        # Simpan data balita dengan ID unik
        data = {
            "ibu": ibu,
            "nama": nama,
            "telepon": telepon,
            "umur": umur,
        }
        # Simpan ke Firebase dengan ID unik untuk setiap entri
        self.db.child("balita").child(username).push(data)  # Menggunakan push untuk menambahkan entri baru

    def ambil_data_balita(self, username):
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

    def simpan_data_bumil(self, username, nama, suami, alamat, telepon):
        # Simpan data bumil dengan ID unik
        data = {
            "nama": nama,
            "suami": suami,
            "alamat": alamat,
            "telepon": telepon,
        }
        # Simpan ke Firebase dengan ID unik untuk setiap entri
        self.db.child("bumil").child(username).push(data)  # Menggunakan push untuk menambahkan entri baru

    def ambil_data_bumil(self, username):
        # Inisialisasi list untuk menyimpan data bumil
        data_bumil = []
        
        try:
            # Mengambil data bumil dari Firebase di bawah node 'bumil/username'
            bumil_data = self.db.child("bumil").child(username).get()
            
            # Periksa apakah ada data
            if bumil_data.each() is not None:
                # Loop melalui setiap entri data bumil
                for bumil in bumil_data.each():
                    # Tambahkan data bumil ke dalam list
                    data_bumil.append(bumil.val())
            else:
                print("Tidak ada data untuk username ini.")
                
        except Exception as e:
            print(f"Error saat mengambil data dari Firebase: {e}")

        # Kembalikan list data bumil
        return data_bumil
    
    def simpan_data_perkembangan(self, username, nama, berat, lingkarK, tinggi, lingkarl):
        # Simpan data bumil dengan ID unik
        data = {
            "Nama": nama,
            "Berat": berat,
            "Lingkar": lingkarK,
            "Tinggi": tinggi,
            "Lingkar": lingkarl
        }
        # Simpan ke Firebase dengan ID unik untuk setiap entri
        self.db.child("adddata").child(username).push(data)  # Menggunakan push untuk menambahkan entri baru
        
    def ambil_data_perkembangan(self, username):
        # Inisialisasi list untuk menyimpan data bumil
        data_perkembangan = []
        
        try:
            # Mengambil data bumil dari Firebase di bawah node 'bumil/username'
            adddata_data = self.db.child("adddata").child(username).get()
            
            # Periksa apakah ada data
            if adddata_data.each() is not None:
                # Loop melalui setiap entri data bumil
                for adddata in adddata_data.each():
                    # Tambahkan data bumil ke dalam list
                    adddata_data.append(adddata.val())
            else:
                print("Tidak ada data untuk username ini.")
                
        except Exception as e:
            print(f"Error saat mengambil data dari Firebase: {e}")

        # Kembalikan list data bumil
        return adddata_data