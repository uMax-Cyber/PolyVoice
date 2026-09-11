#!/usr/bin/env python3
"""Multilingual TTS: splits text by language, synthesizes each segment,
concatenates with ffmpeg. Voices: ru/en/uz."""
import asyncio, os, re, subprocess, tempfile

VOICE_MAP = {
    "ru": "ru-RU-DmitryNeural",
    "en": "en-US-AndrewNeural",
    "uz": "uz-UZ-SardorNeural",
}
UZ_HINTS = re.compile(
    r"\b(salom|bolla|bratan|qanday|yaxshi|rasm|kerak|qil|bor|yo'q|tushunarli|rahmat)\b",
    re.IGNORECASE)

def detect_language(seg):
    if re.search(r"[Ѐ-ӿ]", seg): return "ru"
    if not re.findall(r"[A-Za-z]+", seg): return "ru"
    if len(UZ_HINTS.findall(seg)) >= 2: return "uz"
    return "en"

def split_segments(text):
    """Split into (lang, text) runs by script boundaries."""
    runs, cur, cur_script = [], "", None
    for ch in text:
        script = "cyr" if re.match(r"[Ѐ-ӿ]", ch) else \
                 ("lat" if ch.isascii() and ch.isalpha() else None)
        if script is None: cur += ch; continue
        if cur_script is None: cur_script = script
        if script == cur_script: cur += ch
        else:
            if cur.strip(): runs.append(cur)
            cur, cur_script = ch, script
    if cur.strip(): runs.append(cur)
    out = []
    for r in runs:
        lang = detect_language(r)
        if out and out[-1][0] == lang:
            out[-1] = (lang, out[-1][1] + " " + r)
        else: out.append((lang, r))
    return out

async def synthesize(text, output_path):
    import edge_tts
    segments = split_segments(text)
    if len(segments) <= 1:
        lang = segments[0][0] if segments else "ru"
        await edge_tts.Communicate(text, VOICE_MAP[lang]).save(output_path)
        return output_path
    # Multi-language: synthesize per segment, concat
    tmpdir = tempfile.mkdtemp()
    parts = []
    for i, (lang, seg) in enumerate(segments):
        part = os.path.join(tmpdir, f"part{i:02d}.mp3")
        await edge_tts.Communicate(seg, VOICE_MAP[lang]).save(part)
        parts.append(part)
    lst = os.path.join(tmpdir, "list.txt")
    with open(lst, "w") as f:
        for p in parts: f.write(f"file '{p}'\n")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat",
                    "-safe", "0", "-i", lst, "-c:a", "libmp3lame",
                    "-q:a", "4", output_path], check=True)
    return output_path

if __name__ == "__main__":
    import sys
    text = sys.argv[1] if len(sys.argv) > 1 else "Привет! Hello! Salom!"
    out = sys.argv[2] if len(sys.argv) > 2 else "/tmp/tts_output.mp3"
    asyncio.run(synthesize(text, out))
    print(f"saved: {out}")
