<div align="center">

[![English](https://img.shields.io/badge/README-English-blue)](README.md)
[![Русский](https://img.shields.io/badge/README-Русский-red)](README.ru.md)
[![Oʻzbekcha](https://img.shields.io/badge/README-Oʻzbekcha-green)](README.uz.md)

</div>

# Koʻp tilli TTS + STT konveyeri
[![CI](https://github.com/uMax-Cyber/PolyVoice/actions/workflows/ci.yml/badge.svg)](https://github.com/uMax-Cyber/PolyVoice/actions/workflows/ci.yml)


![Namoyish](screenshots/demo.svg)
AI-agentlar uchun uch tilli (rus/ingliz/oʻzbek) matndan nutq sintezi (TTS) va nutqni tanish (STT) konveyeri. Aralash matn kiritialarini («bratan, nado sdelat legacy project, salom bolla») har bir segment uchun tilni avtomatik aniqlash bilan qayta ishlaydi.

## ✨ Imkoniyatlar

- **Har bir segment uchun tilni avtomatik aniqlash** — kirill yoki lotin yozuvi, oʻzbek tili uchun esa leksik ishoralar
- **Bepul TTS** — Microsoft Edge neyron ovozlarida (API kalitsiz, mutlaqo bepul)
- **Ishonchli STT** — asosiy dvigatel sifatida GigaAM Multilingual va zaxira sifatida faster-whisper
- **Buzuqlikni aniqlash** — til almashtirishdagi xatolarni sezib, natijani zaxira dvigatel bilan qayta oladi
- **Bitta chiqish fayli** — alohida segmentlar audioi ffmpeg orqali bitta faylga birlashtiriladi

## Arxitektura

### TTS (matndan nutqga)
```
Kirish matni → Yozuv turini aniqlash (kirill/lotin) → Segmentlarga boʻlish
→ Har bir segment uchun ovoz sintezi (edge-tts, bepul) → ffmpeg bilan birlashtirish → Bitta audio
```

- **Ovozlar**: ru-RU-DmitryNeural, en-US-AndrewNeural, uz-UZ-SardorNeural
- **Aniqlash**: kirill → rus; lotin → ingliz yoki oʻzbek (leksik ishoralar: salom, bolla, rahmat…)
- **Nol xarajat**: Microsoft Edge TTS ishlatiladi (bepul, API kalitsiz)

### STT (nutqdan matnga)
```
Kirish audiosi → GigaAM multilingual (asosiy, 0.5 s) → Sifatni tekshirish
→ Agar buzilgan boʻlsa → Zaxira Whisper → Eng yaxshi natija
```

- **Asosiy dvigatel**: GigaAM Multilingual (Sberning ochiq modeli, MIT litsenziyasi)
- **Zaxira**: faster-whisper small
- **Sifatni tekshirish**: aralash yozuvli buzilishlarni aniqlash (masalan, «bатаn помоi» = til almashtirishdagi xato)

## Ishlab chiqarishdan asosiy xulosalar

1. **GigaAM oʻzbek tilida Whisperrdan yaxshiroq** (lotin yozuvida): Whisper oʻzbek tilini forschadan farqlay olmaydi; GigaAM buni mukammal bajaramoqda
2. **Til almashtirish — eng qiyin holat**: rus va oʻzbek tillari bitta yozuvda aralashsa, GigaAM buzilgan matn chiqaradi — bunda Whisper yaxshiroq ishlaydi
3. **Edge TTS bepul va yetarlicha yaxshi**: agentning ovozli javoblari uchun pulli APIlarga ehtiyoj yoʻq

## Oʻrnatish

```bash
# TTS (edge-tts)
pip install edge-tts

# STT (GigaAM)
git clone https://github.com/salute-developers/GigaAM.git
pip install -e GigaAM[torch]
```

## Foydalanish

```bash
# Matn va chiqish fayli (standart qiymatlar)
python3 scripts/tts_multilang.py "Привет! Hello! Salom!" /tmp/tts_output.mp3

# Aralash kirish — segmentlar alohida aniqlanadi va ovozlashtiriladi
python3 scripts/tts_multilang.py "bratan, nado sdelat legacy project, salom bolla" out.mp3
```

Bir nechta segmentni birlashtirish uchun PATHda `ffmpeg` boʻlishi kerak.

## Litsenziya
MIT

## 📬 Aloqa

Savollaringiz bormi? Yozing: **[allumaxmail@gmail.com](mailto:allumaxmail@gmail.com)**

---

<div align="center">

[![English](https://img.shields.io/badge/README-English-blue)](README.md)
[![Русский](https://img.shields.io/badge/README-Русский-red)](README.ru.md)
[![Oʻzbekcha](https://img.shields.io/badge/README-Oʻzbekcha-green)](README.uz.md)

</div>
