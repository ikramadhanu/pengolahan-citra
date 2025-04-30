def load_bmp(filename):
    with open(filename, 'rb') as f:
        header = f.read(54)  # BMP header
        data = bytearray(f.read())
    return header, data

def save_bmp(filename, header, data):
    with open(filename, 'wb') as f:
        f.write(header)
        f.write(data)

def convert_to_grayscale(data):
    # Setiap pixel BMP 24-bit: 3 byte (B, G, R)
    for i in range(0, len(data), 3):
        b = data[i]
        g = data[i + 1]
        r = data[i + 2]

        # Grayscale brightness (standar luminansi)
        gray = int(0.114 * b + 0.587 * g + 0.299 * r)

        # Set ketiganya ke nilai grayscale
        data[i] = data[i + 1] = data[i + 2] = gray

    return data

def main():
    input_file = input("Masukkan nama file BMP yang ingin dikonversi (misal: foto.bmp): ")
    output_file = "grayscale_" + input_file

    try:
        header, data = load_bmp(input_file)
        grayscale_data = convert_to_grayscale(data)
        save_bmp(output_file, header, grayscale_data)
        print("Gambar berhasil dikonversi ke grayscale. Disimpan sebagai:", output_file)
    except FileNotFoundError:
        print("File tidak ditemukan.")
    except Exception as e:
        print("Terjadi kesalahan:", e)

# Jalankan
main()
