# Auto Typing Tool

## Deskripsi
Auto Typing Tool adalah aplikasi desktop yang membantu Anda meng-otomatisasi proses pengetikan teks. Aplikasi ini dirancang untuk mengetik teks secara otomatis ke aplikasi lain dengan kecepatan yang dapat disesuaikan, sangat berguna untuk mengatasi tugas pengetikan berulang.

## Fitur Utama
- **Tiga metode pengetikan**: Per karakter, Batch, atau menggunakan Keyboard API
- **Pengaturan kecepatan yang dapat disesuaikan**
- **Timer penundaan** sebelum mulai mengetik
- **Selalu di atas (Always on top)** agar mudah diakses
- **Antarmuka pengguna yang intuitif** dengan tab Editor dan Pengaturan
- **Status pengetikan** yang dapat dipantau
- **Tombol stop** untuk menghentikan pengetikan kapan saja

## Instalasi
1. Unduh file [AutoTypingBot_Installer.exe](https://github.com/lukman754/Auto-Typing/releases/download/v1.0/AutoTypingBot_Installer.exe)
2. Jalankan file installer dan ikuti petunjuk di layar
3. Setelah instalasi selesai, Anda dapat menjalankan aplikasi dari menu Start atau dari shortcut di desktop

## Cara Penggunaan

### Langkah Dasar
1. Buka aplikasi Auto Typing Tool
2. Masukkan teks yang ingin diketik secara otomatis pada area editor
3. Atur delay awal sebelum pengetikan dimulai (defaultnya 3 detik)
4. Klik tombol "Mulai"
5. Segera tempatkan kursor Anda di tempat yang Anda inginkan untuk teks diketik (misalnya dokumen Word, form web, dll)
6. Tunggu hingga hitungan mundur selesai dan pengetikan akan dimulai secara otomatis

### Pengaturan Metode Pengetikan
Pilih salah satu metode pengetikan pada tab Pengaturan:

#### 1. Karakter (Character by Character)
- Mengetik satu karakter pada satu waktu
- Lebih lambat tapi lebih stabil
- Sesuaikan "Delay per karakter" untuk mengatur kecepatan

#### 2. Batch (Default)
- Mengetik beberapa karakter sekaligus dalam satu batch
- Lebih cepat tapi mungkin sedikit buffer
- Sesuaikan "Ukuran batch" dan "Delay antar batch" sesuai kebutuhan

#### 3. Keyboard API
- Menggunakan API keyboard untuk pengetikan sangat cepat
- Metode tercepat yang tersedia
- Hampir tidak ada delay antar karakter

### Tips Penggunaan
- Gunakan fitur "Always on Top" untuk menjaga aplikasi tetap terlihat di atas jendela lain
- Untuk teks yang panjang, pilih metode Batch atau Keyboard API
- Gunakan tombol "Stop" jika ingin menghentikan proses pengetikan
- Tombol "Bersihkan" akan menghapus semua teks dari editor

## Pemecahan Masalah

### Jika aplikasi tidak mengetik:
1. Pastikan kursor Anda berada pada aplikasi target yang benar
2. Coba tingkatkan nilai delay sebelum pengetikan untuk memberikan waktu lebih banyak
3. Periksa apakah aplikasi target menerima input dari alat eksternal

### Jika pengetikan terlalu cepat:
1. Pilih metode "Karakter" dan tingkatkan delay per karakter
2. Untuk metode "Batch", kurangi ukuran batch atau tingkatkan delay antar batch

### Jika pengetikan terlalu lambat:
1. Gunakan metode "Keyboard API" untuk pengetikan tercepat
2. Atau gunakan metode "Batch" dengan ukuran batch lebih besar dan delay lebih kecil
