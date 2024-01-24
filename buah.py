import turtle

# Inisialisasi tampilan Turtle
layar = turtle.Screen()
layar.title("Bendera Palestina")
layar.bgcolor("white")

# Membuat turtle
bendera = turtle.Turtle()
bendera.speed(0)
bendera.penup()
bendera.hideturtle()

# Warna-warna bendera
warna_hitam = "#000000"  # Hitam dalam kode hex
warna_putih = "#ffffff"  # Putih dalam kode hex
warna_hijau = "#009C3B"  # Hijau dalam kode hex
warna_merah = "#BF0A30"  # Merah dalam kode hex

# Dimensi bendera Palestina
lebar = 600
tinggi = 400

# Fungsi untuk menggambar satu bagian vertikal bendera
def gambar_bagian_vertikal(warna, x, y, lebar, tinggi):
    bendera.color(warna)
    bendera.goto(x, y)
    bendera.begin_fill()
    for _ in range(2):
        bendera.forward(lebar)
        bendera.left(90)
        bendera.forward(tinggi)
        bendera.left(90)
    bendera.end_fill()

# Menggambar warna hitam (bagian kiri)
gambar_bagian_vertikal(warna_hitam, -lebar / 2, -tinggi / 2, lebar / 2, tinggi)

# Menggambar warna hijau (bagian kanan)
gambar_bagian_vertikal(warna_hijau, 0, -tinggi / 2, lebar / 2, tinggi)

# Menambahkan teks "FREE PALESTINE"
bendera.penup()
bendera.color(warna_putih)
bendera.goto(0, tinggi / 3.5)  # Atur posisi teks di atas bendera
bendera.write("FREE PALESTINE", align="center", font=("Arial", 24, "bold"))

# Menutup jendela jika diklik
layar.exitonclick()
