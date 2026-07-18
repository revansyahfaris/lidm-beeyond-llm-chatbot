import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
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

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # nanti persempit ke domain kamu saat production
    allow_methods=["*"],
    allow_headers=["*"],
)

# Riwayat percakapan disimpan sederhana di memory, per session_id
sessions = {}

def get_session_history(session_id: str):
    if session_id not in sessions:
        sessions[session_id] = [
            {"role": "system", "content": system_instruction}
        ]
    return sessions[session_id]

class ChatRequest(BaseModel):
    message: str
    session_id: str = "default"

class ChatResponse(BaseModel):
    reply: str

@app.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest):
    history = get_session_history(req.session_id)
    history.append({"role": "user", "content": req.message})

    response = llm.create_chat_completion(
        messages=history,
        temperature=0.5,
        max_tokens=200
    )

    reply = response["choices"][0]["message"]["content"]
    history.append({"role": "assistant", "content": reply})

    return ChatResponse(reply=reply)