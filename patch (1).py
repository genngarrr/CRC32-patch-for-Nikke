import os

FILE_PATH = "service_core.dll" 
BACKUP_PATH = FILE_PATH + ".bak"

TARGET_SEQUENCE = bytes.fromhex("18 75 2A C6 45 FC 03 8D") 


REPLACEMENT_SEQUENCE = bytes.fromhex("18 90 90 C6 45 FC 03 8D")

def patch_launcher():
    if not os.path.exists(FILE_PATH):
        print(f" File {FILE_PATH} not found.")
        return

    if not os.path.exists(BACKUP_PATH):
        print(f"A backup is being created: {BACKUP_PATH}")
        with open(FILE_PATH, 'rb') as src, open(BACKUP_PATH, 'wb') as dst:
            dst.write(src.read())

    with open(FILE_PATH, 'rb') as f:
        file_data = f.read()

    match_count = file_data.count(TARGET_SEQUENCE)
    
    if match_count == 0:
        print("Unique signature not found.")
        return
    elif match_count > 1:
        print(f"the signature matched {match_count} times")
        return

    patched_data = file_data.replace(TARGET_SEQUENCE, REPLACEMENT_SEQUENCE)

    with open(FILE_PATH, 'wb') as f:
        f.write(patched_data)
        
    print("ready")

if __name__ == "__main__":
    patch_launcher()