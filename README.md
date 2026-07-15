# 🤖 Buddy - AI English Learning Companion

**Buddy** adalah chatbot interaktif berbasis AI lokal yang dirancang khusus sebagai teman belajar dan mengobrol interaktif untuk anak-anak Indonesia yang baru mulai belajar Bahasa Inggris (tingkat dasar/pemula).

Menggunakan model **Qwen2.5-7B-Instruct.Q4_K_M** yang berjalan secara lokal (100% offline) menggunakan library `llama-cpp-python`, chatbot ini mampu memberikan respons yang ceria, memberikan misi kosakata harian, serta membimbing anak secara ramah tanpa membebani mereka dengan kalimat bahasa Inggris yang rumit.

---

## ✨ Fitur Utama

- **100% Lokal & Offline:** Berjalan langsung di laptop/komputer tanpa memerlukan koneksi internet atau API key berbayar.
- **Ramah Anak (Child-Friendly Persona):** Bahasa pengantar menggunakan Bahasa Indonesia yang ceria, penuh emoji, dan suportif.
- **Metode Belajar Terstruktur:** Mengikuti pola *Puji Jawaban ➔ Ajarkan Kosakata Baru ➔ Berikan Misi/Tantangan Baru*.
- **Optimasi CPU:** Menggunakan format kuantisasi GGUF (`Q4_K_M`) yang sangat ringan dan cepat meskipun dijalankan tanpa dedicated GPU.

---

## 🛠️ Prasyarat & Instalasi

### 1. Kloning atau Siapkan Folder Proyek

Pastikan script `app.py` berada di dalam satu folder khusus.

### 2. Unduh Model GGUF

Unduh file model **Qwen2.5-7B-Instruct.Q4_K_M.gguf** dari Hugging Face (misalnya dari repositori resmi Qwen atau Bartowski). Setelah diunduh, **pindahkan file model tersebut ke dalam folder yang sama dengan proyek ini**.

Struktur folder Anda harus terlihat seperti ini:

```text
nama-proyek-anda/
├── app.py
└── qwen2.5-7b-instruct-q4_k_m.gguf
```

### 3. Install Dependencies

Buka terminal/command prompt di dalam folder proyek tersebut, kemudian install library yang dibutuhkan:

**Untuk Pengguna CPU Saja (Rekomendasi Standar):**

```bash
pip install llama-cpp-python
```

**Untuk Pengguna GPU NVIDIA (Akselerasi CUDA):**

Jika Anda memiliki GPU NVIDIA dan ingin proses pembuatan teks menjadi lebih instan, install dengan perintah berikut:

```bash
CMAKE_ARGS="-GGML_CUDA=on" pip install llama-cpp-python --upgrade --force-reinstall --no-cache-dir
```

---

## 🚀 Cara Menjalankan

Setelah semua instalasi selesai dan file model sudah berada di folder yang benar, jalankan perintah berikut di terminal:

```bash
python app.py
```

### 🎮 Contoh Interaksi di Terminal

```text
Memuat Buddy, Teman Belajar Bahasa Inggris... 🚀

Buddy: Halo Teman Pintar! ✨ Namaku Buddy, robot yang siap menemani kamu belajar bahasa Inggris jadi seru banget! Hari ini kita akan belajar tentang "Aktivitas Sehari-hari". Misi pertama kamu: coba sebutkan satu kegiatan yang paling kamu suka lakukan di pagi hari? ☀️

Anak: aku suka makan buah
Buddy: Wah, makan buah ya? Sehat dan hebat sekali! ✨ Dalam bahasa Inggris, "Makan" itu EAT (dibaca: it). Nah, sekarang kalau setelah makan kita mau belajar, coba tebak bahasa Inggrisnya "Belajar" apa hayo? 📚
```

> Untuk menyudahi percakapan, Anda cukup mengetik `keluar`, `exit`, atau `quit` pada kolom input anak.

---

## ⚙️ Kustomisasi Materi Pembelajaran

Anda dapat mengubah topik atau daftar kosakata yang ingin diujikan kepada anak secara dinamis dengan mengedit bagian **`system_instruction`** di dalam file `app.py`:

```python
# Ubah bagian ini sesuai topik kurikulum yang diinginkan
system_instruction = """
...
3. KOSAKATA HARI INI: Fokus pada tema "Nama-nama Hewan" (Contoh kata dasar: cat, dog, fish, bird). Jangan gunakan kata-kata sulit di luar itu.
...
"""
```

---

## 📄 Lisensi

Proyek ini dikembangkan untuk tujuan edukasi open-source. Model dasar menggunakan model Qwen2.5 dari Alibaba Cloud yang dilisensikan di bawah Apache 2.0.