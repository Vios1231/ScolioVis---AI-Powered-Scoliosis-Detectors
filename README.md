# 🩻 ScolioVis: Scoliosis Detection Web App

ScolioVis adalah aplikasi web berbasis **Flask + TensorFlow** untuk mendeteksi kemungkinan skoliosis dari citra X-ray tulang belakang.  
Model CNN dilatih menggunakan dataset dua kelas: `Normal` dan `Scoliosis`.

---

## 🚀 Fitur Utama

- Deteksi skoliosis berbasis **deep learning (VGG16 Transfer Learning)**
- **Web interface** sederhana menggunakan Flask
- Mendukung format gambar `.jpg`, `.jpeg`, `.png`, `.gif`
- Preprocessing otomatis (resize, normalize, convert RGB)
- Akurasi tinggi dengan model final `scoliosis_detection_model_final.keras`

---

## 🧠 Model

Model menggunakan **VGG16** (transfer learning) dengan lapisan tambahan Dense dan Dropout untuk menghindari overfitting.  
Dilatih pada dataset dua kelas (`Normal` dan `Scoliosis`), dengan pembagian:
- `train/`
- `validation/`
- `test/`

(Berada di folder static)
Model disimpan dalam format:
scoliosis_detection_model_fixed.keras


---

## ⚙️ Instalasi

1. Clone repositori:
   ```bash
   git clone https://github.com/<your-username>/ScolioVis.git
   cd ScolioVis

2. Aktifkan Enviroment:
   ```bash
   python -m venv venv
   venv\Scripts\activate      # Windows
   atau
   source venv/bin/activate   # Mac/Linux

3. Installasi Requirements:
   ```bash
   pip install -r requirements.txt

5. Jalankan python app.py
   ```bash
   python app.py
   ```

## 🌐 Penggunaan

1. Buka browser dan akses:
   ```bash
   http://127.0.0.1:5000

2. Upload gambar X-ray (format: .jpg, .png, .jpeg, .gif).

3. Tunggu hasil prediksi:
   ```bash
   ✅ Normal Detected
   ⚠️ Scoliosis Detected
   ```

## Screenshot DEMO
<img width="1904" height="1042" alt="Screenshot 2025-11-05 005259" src="https://github.com/user-attachments/assets/6f840805-9037-4b03-8406-b93b17aeb0c8" />
<img width="1888" height="1035" alt="Screenshot 2025-11-05 005314" src="https://github.com/user-attachments/assets/d42e6039-0fa7-41da-a628-460808f6cde0" />
<img width="1883" height="1040" alt="Screenshot 2025-11-05 005330" src="https://github.com/user-attachments/assets/3f10857a-f326-4d28-88cb-e6522bdcac1d" />
<img width="1877" height="1009" alt="Screenshot 2025-11-05 005404" src="https://github.com/user-attachments/assets/7d75a8bd-08e3-4000-934f-50edf587fb0d" />
<img width="1890" height="472" alt="Screenshot 2025-11-05 005446" src="https://github.com/user-attachments/assets/014f8038-0066-4eab-b612-4c4952be0bb3" />

## 📁 Struktur Folder
```bash
ScolioVis/
│
├── app.py
├── requirements.txt
├── static/
│   └── scoliosis_detection_model_final.keras
├── templates/
│   ├── index.html
│   ├── about.html
│   └── paper.html
└── README.md
```

## 🧑‍💻 Pengembang

Jonathan Alvios, Hernicksen Satria, Andy Saputra | Binus University Alam Sutera  
Penelitian Model Deteksi Skoliosis Berbasis CNN  

## 📜 Lisensi

MIT License © 2025 — Bebas digunakan untuk penelitian, pengembangan, dan edukasi.
