import os
from datetime import datetime

# CONFIGURATION

input_m3u = r"Z:\PLACE HOLDER"   # input .m3u file / text file to change directory of
phone_music_dir = "E.G. /storage/emulated/0/Music/Songs/"      # Starting directory of input file to change

def get_clean_pc_directory():
    while True:
        pc_dir = "Z:/".strip()  # the directory you want to change the phone_music_dir with (e.g. Z:/)
        if not pc_dir:
            print("Directory path cannot be empty. Try again.")
        elif not os.path.exists(pc_dir):
            print("Warning: This path does not exist. Please check and try again.")
        else:
            return pc_dir.replace("\\", "/").rstrip("/") + "/"

def generate_output_filename(input_file):
    # Get the directory of the input file
    input_dir = os.path.dirname(input_file)
    # Get the base name without extension
    base_name = os.path.splitext(os.path.basename(input_file))[0]
    today = datetime.now().strftime("%d%m%Y")  # UK format: DDMMYYYY
    # Create the full path in the same directory as input file
    return os.path.join(input_dir, f"{base_name}_{today}_PC.m3u")

def fix_playlist_paths(input_file, old_path, new_path):
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

# MAIN EXECUTION
print("=== M3U Path Fixer with File Check ===")
pc_music_dir = get_clean_pc_directory()
fix_playlist_paths(input_m3u, phone_music_dir, pc_music_dir)
