import hashlib

def calculate_hashes(file_path):
    hashes = {
        'MD5': hashlib.md5(),
        'SHA1': hashlib.sha1(),
        'SHA256': hashlib.sha256()
    }

    try:
        with open(file_path, 'rb') as f:
            while chunk := f.read(8192):
                for h in hashes.values():
                    h.update(chunk)

        for name, h in hashes.items():
            print(f"{name}: {h.hexdigest()}")

    except FileNotFoundError:
        print("❌ File not found.")
    except Exception as e:
        print(f"⚠️ Error: {e}")

if __name__ == "__main__":
    print("🔍 hashpeek — Simple file hash analyzer")
    path = input("📄 Enter file path: ")
    calculate_hashes(path)
