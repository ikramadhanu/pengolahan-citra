from PIL import Image
from tkinter import filedialog
import tkinter as tk
import os

def buka_gambar():
    root = tk.Tk()
    root.withdraw()
    filepath = filedialog.askopenfilename(
        title="Pilih gambar", 
        filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp")]
    )
    return filepath

def gambar_ke_citra_biner(path, threshold=128, simpan=True):
    img = Image.open(path).convert('L')  # grayscale
    width, height = img.size
    pixels = img.load()

    print(f"\nUkuran gambar: {width} x {height}")
    print("Citra biner:")

    # Gambar baru hitam-putih
    hasil_img = Image.new('1', (width, height))

    for y in range(height):
        for x in range(width):
            abu = pixels[x, y]
            if abu > threshold:
                hasil_img.putpixel((x, y), 1)
                print("1", end="")
            else:
                hasil_img.putpixel((x, y), 0)
                print("0", end="")
        print()

    if simpan:
        # Ambil nama file asli tanpa ekstensi
        nama_asli = os.path.splitext(os.path.basename(path))[0]
        nama_output = f"{nama_asli}_biner.png"
        hasil_img.save(nama_output)
        print(f"\nGambar biner disimpan sebagai '{nama_output}'")

# Jalankan
path = buka_gambar()
if path:
    gambar_ke_citra_biner(path, threshold=128)
else:
    print("Tidak ada gambar yang dipilih.")
