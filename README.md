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

---

## 📁 Contoh Struktur File Akun (`akunX.json`)

```json
{
  "MINES": {
    "EARTH": {
      "mine_id": "06890dbc-5d47-7ae1-8000-0e66f2610153"
    }
  },
  "FACTORIES": {
    "MUD 1": {
      "factory_id": "06891bba-2b02-70c4-8000-f06a87253945"
    },
    "CLAY 1": {
      "factory_id": "06891d63-328f-75c2-8000-ff149ed8ec78"
    },
    ...//dan seterusnya
  },
  "UPGRADES": {
    "MUD 1": {
      "factory_id": "06891bba-2b02-70c4-8000-f06a87253945"
    },
    "CLAY 1": {
      "factory_id": "06891d63-328f-75c2-8000-ff149ed8ec78"
    },
    ...//dan seterusnya
  },
  "CLAIM_AREAS": {
    "MUD": {
      "area_id": "06891b3f-2add-72f1-8000-76f91ad17502"
    },
    "CLAY": {
      "area_id": "06891e01-2e89-7ac4-8000-706e1969499d"
    },
    ...//dan seterusnya
  },
  "CLAIMS": {
    "EARTH": {
      "mine_id": "06890dbc-5d47-7ae1-8000-0e66f2610153"
    }
  },
  "UPGRADE_MINES": {
    "EARTH": {
      "mine_id": "06890dbc-5d47-7ae1-8000-0e66f2610153"
    }
  }
}
```

---

## 🔍 Keterangan Penting:

- Nama seperti `"EARTH"`, `"MUD 1"` hanyalah label bebas (alias). Kamu bisa ganti jadi `"TANAH"`, `"LEMPUNG A"`, dll.
- Nilai ID (`mine_id`, `factory_id`, `area_id`) harus diambil dari DevTools di akun masing-masing (Inspect → Network).
- **Jangan ubah nilai ID sembarangan.** Salah ID = bot gagal.
- Gunakan struktur JSON dengan teliti, tanda `{}`, `:`, dan `,` harus sesuai.

---

## ⚠️ Catatan Multi Akun

Untuk menjalankan **lebih dari satu akun**, buat file baru untuk setiap akun:

```
akun1.json
akun2.json
akun3.json
...
```

> ⚠️ Setiap akun punya ID berbeda.
>
> Kamu wajib mengambil ulang semua `mine_id`, `factory_id`, dan `area_id` dari akun masing-masing.
>
> ❌ Jangan salin ID dari akun lain  
> ✅ Harus ambil manual lewat DevTools setiap akun

---

## 🧠 Ingat!

- **`MINES`, `CLAIMS`, dan `UPGRADE_MINES` hanya butuh 1 ID per akun.**
- **`FACTORIES`, `UPGRADES`, dan `CLAIM_AREAS` bisa lebih dari 1, sesuai jumlah bangunan di akunmu.**
- Buat file akun serapi mungkin agar bot bisa membaca dan eksekusi dengan benar.


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

Aktifkan/Nonaktifkan fitur upgrade otomatis pada file `main.py`. Cari bagian berikut:

```python
# Aktifkan fitur upgrade otomatis (jika perlu)
ENABLE_UPGRADE_FACTORY = True
ENABLE_UPGRADE_MINE = True
```

- Jika tidak ingin upgrade otomatis, ubah `True` menjadi `False`.
- Pastikan kamu mengedit file `main.py`, bukan file lain.

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

Dibuat oleh [@kontolkuda](https://t.me/jamalnggau36)  
Kontribusi, ide, dan feedback sangat diterima!
