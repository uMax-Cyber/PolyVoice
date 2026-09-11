<div align="center">

[![English](https://img.shields.io/badge/README-English-blue)](README.md)
[![Русский](https://img.shields.io/badge/README-Русский-red)](README.ru.md)
[![Oʻzbekcha](https://img.shields.io/badge/README-Oʻzbekcha-green)](README.uz.md)

</div>

# Multilingual TTS + STT Pipeline
[![CI](https://github.com/uMax-Cyber/PolyVoice/actions/workflows/ci.yml/badge.svg)](https://github.com/uMax-Cyber/PolyVoice/actions/workflows/ci.yml)


![Demo](screenshots/demo.svg)
Three-language (Russian/English/Uzbek) text-to-speech and speech-to-text pipeline for AI agents. Handles mixed-language input ("bratan, nado sdelat legacy project, salom bolla") with automatic language detection per segment.

## ✨ Features

- **Automatic language detection** per segment — Cyrillic vs Latin script plus lexical hints for Uzbek
- **Free TTS** via Microsoft Edge neural voices (no API key, zero cost)
- **Robust STT** with GigaAM multilingual as primary and faster-whisper as fallback
- **Garble detection** — catches code-switching failures and retries with the fallback engine
- **Single output file** — per-segment audio stitched together with ffmpeg

## Architecture

### TTS (Text-to-Speech)
```
Input text → Script detection (Cyrillic/Latin) → Language segmentation
→ Per-segment voice synthesis (edge-tts, free) → ffmpeg concat → Single audio
```

- **Voices**: ru-RU-DmitryNeural, en-US-AndrewNeural, uz-UZ-SardorNeural
- **Detection**: Cyrillic → Russian; Latin → English or Uzbek (lexical hints: salom, bolla, rahmat...)
- **Zero cost**: Uses Microsoft Edge TTS (free, no API key)

### STT (Speech-to-Text)
```
Audio input → GigaAM multilingual (primary, 0.5s) → Quality check
→ If garbled → Whisper fallback → Best result
```

- **Primary**: GigaAM Multilingual (Sber's open model, MIT license)
- **Fallback**: faster-whisper small
- **Quality check**: Mixed-script garble detection (e.g., "bатаn помоi" = code-switching failure)

## Key Insights from Production

1. **GigaAM beats Whisper for Uzbek** (Latin script): Whisper confuses Uzbek with Farsi; GigaAM handles it perfectly
2. **Code-switching is the hard case**: GigaAM produces mojibake when Russian and Uzbek mix in one clip — Whisper handles this better
3. **Edge TTS is free and good enough**: No need for paid APIs for agent voice responses

## Setup

```bash
# TTS (edge-tts)
pip install edge-tts

# STT (GigaAM)
git clone https://github.com/salute-developers/GigaAM.git
pip install -e GigaAM[torch]
```

## Usage

```bash
# Text argument + output file (defaults shown)
python3 scripts/tts_multilang.py "Привет! Hello! Salom!" /tmp/tts_output.mp3

# Mixed-language input — segments are detected and voiced separately
python3 scripts/tts_multilang.py "bratan, nado sdelat legacy project, salom bolla" out.mp3
```

Requires `ffmpeg` on PATH for multi-segment concatenation.

## License
MIT

## 📬 Contact

Questions? Reach out: **[allumaxmail@gmail.com](mailto:allumaxmail@gmail.com)**

---

<div align="center">

[![English](https://img.shields.io/badge/README-English-blue)](README.md)
[![Русский](https://img.shields.io/badge/README-Русский-red)](README.ru.md)
[![Oʻzbekcha](https://img.shields.io/badge/README-Oʻzbekcha-green)](README.uz.md)

</div>
