<div align="center">

**🇬🇧 [English](README.md) · 🇷🇺 [Русский](README.ru.md) · 🇺🇿 [Oʻzbekcha](README.uz.md)**

</div>

# Multilingual TTS + STT Pipeline
[![CI](https://github.com/uMax-Cyber/PolyVoice/actions/workflows/ci.yml/badge.svg)](https://github.com/uMax-Cyber/PolyVoice/actions/workflows/ci.yml)


![Demo](screenshots/demo.svg)
Three-language (Russian/English/Uzbek) text-to-speech and speech-to-text pipeline for AI agents. Handles mixed-language input ("bratan, nado sdelat legacy project, salom bolla") with automatic language detection per segment.

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

## License
MIT
