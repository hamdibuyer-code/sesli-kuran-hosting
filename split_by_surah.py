import os
import shutil
from pathlib import Path

BASE = Path(r"D:\sesli_kuran_hosting\public\audio_data\Abu_Bakr_Ash-Shaatree")

def main():
    if not BASE.exists():
        raise SystemExit(f"Klasör yok: {BASE}")

    mp3s = list(BASE.glob("*.mp3"))
    if not mp3s:
        raise SystemExit("Bu klasörde .mp3 bulunamadı. Doğru yerde misin?")

    moved = 0
    for f in mp3s:
        name = f.name  # 001001.mp3
        if len(name) < 10 or not name[:6].isdigit():
            continue
        surah = name[:3]  # '001'
        target_dir = BASE / surah
        target_dir.mkdir(parents=True, exist_ok=True)
        target = target_dir / name
        shutil.move(str(f), str(target))
        moved += 1

    print(f"Tasindi: {moved} dosya")
    print("Bitti.")

if __name__ == "__main__":
    main()
