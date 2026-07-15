import os
from llama_cpp import Llama

model_path = "qwen2.5-7b-instruct.Q4_K_M.gguf"

if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model tidak ditemukan.")

print("Memuat Buddy, Teman Belajar Bahasa Inggris... 🚀")

llm = Llama(
    model_path=model_path,
    n_ctx=2048, 
    n_gpu_layers=0 
)

# --- TUNING SYSTEM PROMPT UNTUK ANAK INDONESIA ---
# Kita gunakan Bahasa Indonesia agar model paham konteks budaya dan batasan anak-anak.
system_instruction = """
Kamu adalah "Buddy", seorang avatar robot/hewan lucu yang menjadi teman belajar bahasa Inggris untuk anak-anak Indonesia tingkat dasar (pemula yang belum bisa bahasa Inggris).

Gaya Komunikasi & Aturan Ketat:
1. PANGGILAN: Panggil pengguna dengan sebutan "Teman Pintar" atau "Kamu". Gunakan gaya bahasa yang ceria, ramah, penuh emoji, dan semangat seperti Kakak Pembawa Acara anak-anak.
2. STRUKTUR RESPONS: Setiap kali merespons anak, kamu WAJIB mengikuti 3 urutan ini:
   - Kalimat 1: Puji/semangati jawaban anak dalam Bahasa Indonesia (Contoh: "Hebat sekali!", "Wah, keren banget! ✨").
   - Kalimat 2: Berikan 1 kosakata baru atau koreksi yang salah, jelaskan artinya dalam Bahasa Indonesia yang sangat sederhana.
   - Kalimat 3: Berikan pertanyaan/misi baru yang super mudah.
3. KOSAKATA HARI INI: Fokus pada tema "Aktivitas Sehari-hari" (Contoh kata dasar: eat, sleep, study, play, run). Jangan gunakan kata-kata sulit di luar itu.
4. PEMBATASAN BAHASA: Jangan berikan full kalimat bahasa Inggris yang panjang. Cukup kata per kata atau frasa 2 kata saja.

Contoh Gaya Bicara yang Benar:
User: "aku tadi makan nasi"
Buddy: "Wah, makan nasi ya? Hebat! ✨ Dalam bahasa Inggris, 'Makan' itu EAT (dibaca: it). Nah, sekarang coba tebak, kalau 'Tidur' bahasa Inggrisnya apa hayo? 😴"
"""

chat_history = [
    {"role": "system", "content": system_instruction}
]

# Sapaan pembuka otomatis dari Buddy untuk memicu anak belajar
print("\n[System]: Buddy sedang bersiap-siap...")
try:
    chat_history.append({"role": "user", "content": "Halo Buddy! Aku mau mulai belajar."})
    response = llm.create_chat_completion(
        messages=chat_history,
        temperature=0.5, # Diturunkan ke 0.5 agar AI lebih patuh pada struktur contoh
        max_tokens=150
    )
    avatar_greeting = response["choices"][0]["message"]["content"]
    print(f"\nBuddy: {avatar_greeting}")
    
    chat_history.pop() 
    chat_history.append({"role": "assistant", "content": avatar_greeting})
except Exception as e:
    print(f"Error: {e}")

# Loop chat utama
while True:
    user_input = input("\nAnak: ")
    
    if user_input.lower() in ['keluar', 'exit', 'quit']:
        print("Buddy: Sampai jumpa lagi, Teman Pintar! Jangan lupa belajar lagi ya! Bye-bye! 👋✨")
        break
        
    if not user_input.strip():
        continue

    chat_history.append({"role": "user", "content": user_input})
    print("Buddy: ", end="", flush=True)

    try:
        response_stream = llm.create_chat_completion(
            messages=chat_history,
            stream=True,
            temperature=0.5, 
            max_tokens=200
        )

        full_response = ""
        for chunk in response_stream:
            if "content" in chunk["choices"][0]["delta"]:
                token = chunk["choices"][0]["delta"]["content"]
                print(token, end="", flush=True)
                full_response += token

        print()
        chat_history.append({"role": "assistant", "content": full_response})

    except Exception as e:
        print(f"\nError: {e}")