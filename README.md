# .m3u-path-batch-editor
🎵 Convert mobile .m3u playlist paths to PC-friendly formats with file existence checks — safe, fast, and customizable.

# 🎵 M3U Playlist Path Converter with File Check

A lightweight Python script to convert `.m3u` playlist paths from mobile device format (e.g., Android) to match your PC's file structure — with automatic file existence checks and a clean, timestamped output.

---

## 📌 Features

- ✅ Converts old mobile music paths (e.g. `/storage/emulated/0/Music/`) to PC-friendly paths (e.g. `Z:/Music/`)
- 🔍 Checks if each referenced file actually exists on your PC
- 📝 Saves a new `.m3u` playlist with today’s date appended
- 💡 Designed to be minimal and safe — does **not modify** original playlists
- 🖥️ Works in any modern Python 3 environment (Windows, macOS, Linux)

---

## ⚙️ Setup

### 1. Requirements

- Python 3.6 or later
- No external packages required (`os`, `datetime` used)

---

## ✏️ Configuration

Before running the script, open `playlist_converter.py` and **edit these lines** near the top:

```python
input_m3u = r"Z:\PLACE HOLDER"   # input .m3u file / text file to change directory of     [LINE 6]
phone_music_dir = "E.G. /storage/emulated/0/Music/Songs/"      # Starting directory of input file to change  [LINE 7]
pc_dir = "Z:/".strip()  # the directory you want to change the phone_music_dir with (e.g. Z:/)   [LINE 11]
