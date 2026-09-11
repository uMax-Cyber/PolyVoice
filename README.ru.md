<div align="center">

[![English](https://img.shields.io/badge/README-English-blue)](README.md)
[![Русский](https://img.shields.io/badge/README-Русский-red)](README.ru.md)
[![Oʻzbekcha](https://img.shields.io/badge/README-Oʻzbekcha-green)](README.uz.md)

</div>

# Многоязычный конвейер TTS + STT
[![CI](https://github.com/uMax-Cyber/PolyVoice/actions/workflows/ci.yml/badge.svg)](https://github.com/uMax-Cyber/PolyVoice/actions/workflows/ci.yml)


![Демонстрация](screenshots/demo.svg)
Трёхъязычный (русский/английский/узбекский) конвейер синтеза речи из текста (TTS) и распознавания речи (STT) для AI-агентов. Обрабатывает смешанный ввод («bratan, nado sdelat legacy project, salom bolla») с автоматическим определением языка для каждого сегмента.

## ✨ Возможности

- **Автоматическое определение языка** для каждого сегмента — кириллица или латиница плюс лексические подсказки для узбекского
- **Бесплатный TTS** на нейронных голосах Microsoft Edge (без API-ключа, нулевая стоимость)
- **Надёжное STT** — GigaAM Multilingual как основной движок и faster-whisper как резервный
- **Детекция «каши»** — распознаёт сбои при переключении языков и повторяет распознавание резервным движком
- **Один выходной файл** — аудио отдельных сегментов склеивается в один через ffmpeg

## Архитектура

### TTS (синтез речи)
```
Входной текст → Определение алфавита (кириллица/латиница) → Сегментация по языкам
→ Синтез голосом для каждого сегмента (edge-tts, бесплатно) → Склейка ffmpeg → Один аудиофайл
```

- **Голоса**: ru-RU-DmitryNeural, en-US-AndrewNeural, uz-UZ-SardorNeural
- **Определение языка**: кириллица → русский; латиница → английский или узбекский (лексические подсказки: salom, bolla, rahmat…)
- **Нулевая стоимость**: используется Microsoft Edge TTS (бесплатно, без API-ключа)

### STT (распознавание речи)
```
Входное аудио → GigaAM multilingual (основной, 0.5 с) → Проверка качества
→ Если «каша» → Резервный Whisper → Лучший результат
```

- **Основной движок**: GigaAM Multilingual (открытая модель Сбера, лицензия MIT)
- **Резервный**: faster-whisper small
- **Проверка качества**: детекция смешанно-алфавитной «каши» (например, «bатаn помоi» = сбой переключения языков)

## Ключевые выводы из продакшена

1. **GigaAM обгоняет Whisper на узбекском** (латиница): Whisper путает узбекский с фарси; GigaAM справляется идеально
2. **Переключение языков — сложный случай**: GigaAM выдаёт mojibake, когда русский и узбекский смешаны в одном клипе — Whisper справляется с этим лучше
3. **Edge TTS бесплатен и достаточно хорош**: платные API для голосовых ответов агента не нужны

## Установка

```bash
# TTS (edge-tts)
pip install edge-tts

# STT (GigaAM)
git clone https://github.com/salute-developers/GigaAM.git
pip install -e GigaAM[torch]
```

## Использование

```bash
# Текст и выходной файл (значения по умолчанию)
python3 scripts/tts_multilang.py "Привет! Hello! Salom!" /tmp/tts_output.mp3

# Смешанный ввод — сегменты определяются и озвучиваются по отдельности
python3 scripts/tts_multilang.py "bratan, nado sdelat legacy project, salom bolla" out.mp3
```

Для склейки нескольких сегментов требуется `ffmpeg` в PATH.

## Лицензия
MIT

## 📬 Контакты

Вопросы? Пишите: **[allumaxmail@gmail.com](mailto:allumaxmail@gmail.com)**

---

<div align="center">

[![English](https://img.shields.io/badge/README-English-blue)](README.md)
[![Русский](https://img.shields.io/badge/README-Русский-red)](README.ru.md)
[![Oʻzbekcha](https://img.shields.io/badge/README-Oʻzbekcha-green)](README.uz.md)

</div>
