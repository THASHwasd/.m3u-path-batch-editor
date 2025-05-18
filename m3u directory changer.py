"""
M3U Playlist Path Converter with File Check
Author: ThashWASD
License: MIT

DISCLAIMER:
    This script is provided "as is" without warranty of any kind.
    Use at your own risk. Modify paths and configurations as per your environment.
    Ensure you have backups of your files before running.

USER INSTRUCTIONS — EDIT THESE LINES BEFORE USE:
    Line 28: Set `input_m3u` to your actual .m3u playlist file path on your PC.
    Line 29: Set `phone_music_dir` to the base path used in the original playlist (e.g., from your mobile device).
    Line 39 (optional): Set `pc_dir` default value if you want to avoid prompting.

DESCRIPTION:
    This script reads an M3U playlist file and converts the file paths to match your PC’s
    directory structure, while checking that each song file exists. A new updated playlist
    will be saved with today’s date in the filename. The file is saved in the current working directory —
    usually the folder where you launched this script.
"""

import os
from datetime import datetime

# === CONFIGURATION — EDIT THESE ===

input_m3u = r""  # e.g., r"C:\Users\You\Downloads\my_playlist.m3u"
phone_music_dir = r""  # e.g., r"/storage/emulated/0/Music/"

# === FUNCTIONS ===

def get_clean_pc_directory():
    
   # Prompt for or define the PC music directory path.
   #  Modify below to set a default, or add input() to prompt.
   
    while True:
        pc_dir = "Z:/".strip()  # <-- Optional: Change this to your PC music folder path
        if not pc_dir:
            print("Directory path cannot be empty. Try again.")
        elif not os.path.exists(pc_dir):
            print("Warning: This path does not exist. Please check and try again.")
        else:
            return pc_dir.replace("\\", "/").rstrip("/") + "/"

def generate_output_filename(input_file):
    
    # Generate a timestamped output filename based on the input file name.
    
    base_name = os.path.splitext(os.path.basename(input_file))[0]
    today = datetime.now().strftime("%d%m%Y")  # UK format: DDMMYYYY
    return f"{base_name}_{today}_PC.m3u"

def fix_playlist_paths(input_file, old_path, new_path):
   
   # Replace old paths in the playlist with new paths and check for missing files.
    
    output_file = generate_output_filename(input_file)
    missing_files = []

    try:
        with open(input_file, 'r', encoding='utf-8') as infile, \
             open(output_file, 'w', encoding='utf-8') as outfile:
            for line in infile:
                if line.strip() and not line.startswith('#'):
                    fixed_path = line.replace(old_path, new_path).strip()
                    if not os.path.exists(fixed_path):
                        missing_files.append(fixed_path)
                    outfile.write(fixed_path + "\n")
                else:
                    outfile.write(line)
        
        print(f"\nPlaylist updated and saved to: {output_file}")
        if missing_files:
            print("\nWARNING: The following files were NOT found on your PC:")
            for path in missing_files:
                print(f" - {path}")
        else:
            print("All song paths were found.")
    except FileNotFoundError:
        print(f"Error: Playlist file '{input_file}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# === MAIN EXECUTION ===

if __name__ == "__main__":
    print("=== M3U Path Fixer with File Check ===")
    pc_music_dir = get_clean_pc_directory()
    fix_playlist_paths(input_m3u, phone_music_dir, pc_music_dir)
