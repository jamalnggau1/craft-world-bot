# 🌍 Craft World Automation Bot

Skrip Python otomatis untuk membantu mengelola aktivitas game di [craft-world.gg](https://craft-world.gg) secara massal menggunakan banyak akun.

## 🧩 Fitur Utama

- ⛏️ **Auto mining** untuk semua sumber daya yang tersedia  
- 🏭 **Auto factory** start & upgrade  
- 🗺️ **Auto claim area & mine**  
- 📦 **Auto klaim Vault**  
- 🔁 **Auto refresh token setiap 50 menit menggunakan `refresh_token`**
- 🔀 **Aksi acak & delay manusiawi**
- 🧱 **Emojifikasi** nama material untuk tampilan lebih informatif  

---

## ⚠️ PERINGATAN PENTING

🚫 **Penggunaan bot ini sangat berisiko menyebabkan akun Anda dibanned oleh pihak Craft World.**  
Gunakan dengan **penuh kesadaran dan tanggung jawab pribadi**.  
> 💡 Disarankan **tidak menggunakan akun utama**, melainkan akun cadangan.

---

## 📁 Struktur File

```
.
├── main.py                    # File utama bot
├── refresh1.txt, refresh2.txt # Wajib! berisi refresh_token & api_key
├── firebase_appcheck.txt      # (Opsional) Token Firebase AppCheck
├── akun1.json, akun2.json     # Data akun (MINES, FACTORIES, dll.)
```

---

## 🔧 Cara Menjalankan

### 1. Install dependensi

```bash
pip install requests rich
```

---

### 2. Buat file refresh token  
Bot ini akan **otomatis membuat & memperbarui token JWT**, jadi kamu **tidak perlu** isi file `token*.txt` secara manual.

Buat file `refresh1.txt`, `refresh2.txt`, dst, dengan format:

```json
{
  "refresh_token": "xxx",
  "api_key": "yyy"
}
```

- `refresh_token` bisa didapat dari inspect browser saat login (Firebase)
- `api_key` = Firebase Web API Key dari project Craft World

---

### 3. (Opsional) Tambahkan Firebase AppCheck

Jika diperlukan, buat file `firebase_appcheck.txt` dan isi dengan:
```
token_appcheck_akun_1
token_appcheck_akun_2
...
```

---

### 4. Siapkan file akun  
Buat file `akun1.json`, `akun2.json`, dst berisi struktur seperti berikut:

```json
{
  "MINES": {
    "CLAY 1": { "mine_id": "abc123" }
  },
  "FACTORIES": {
    "CERAMIC FACTORY": { "factory_id": "def456" }
  },
  "UPGRADES": {},
  "CLAIM_AREAS": {},
  "CLAIMS": {},
  "UPGRADE_MINES": {}
}
```

---

### 5. Jalankan bot

```bash
python main.py
```

Bot akan:
- Refresh token setiap 50 menit
- Menjalankan semua aksi mining, factory, klaim, upgrade, dan vault
- Delay antar aksi untuk meniru perilaku manusia

---

## ⚙️ Konfigurasi Tambahan

Aktifkan fitur upgrade otomatis:

```python
ENABLE_UPGRADE_FACTORY = True
ENABLE_UPGRADE_MINE = True
```

---

## 🧠 Teknologi yang Digunakan

- Python 3
- `requests` – komunikasi API
- `rich` – tampilan CLI berwarna
- JSON file – penyimpanan data akun
- Firebase Identity + AppCheck (token handling)

---

## ❗ Disclaimer

> Proyek ini tidak berafiliasi dengan Craft World.  
> Tujuannya edukasi & eksplorasi API.  
> Gunakan bot ini dengan risiko Anda sendiri – **akun Anda bisa terkena BANNED permanen.**

---

## 💬 Kontak

Dibuat oleh [@username](https://t.me/yourusername)  
Kontribusi, ide, dan feedback sangat diterima!
