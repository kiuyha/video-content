# Menghapus Text pada Gambar

## Cara Kerja
- **Mengambil daftar PATH gambar dalam sebuah folder**.
- **Mengubah resolusi gambar agar tidak melebihi batas 1024 x 1024**.
- **Menyimpan gambar yang telah diubah ke dalam buffer agar tidak mengambil penyimpanan**.
- **Mengubah gambar ke dalam string base 64**
- **Mengirim gambar dalam str base 64 ke client menggunakan API**
- **Mengunduh gambar yang telah diproses dan menyimpannya dalam sebuah folder**.

## NOTE
- ** Kamu harus memiliki Api key yang dapat dipereloh di website [novita.ai](https://novita.ai/settings#key-management) dan simpan di dalam .env file**
- ** Jangan lupa untuk menginstal Python client library nya**
    ```bash
    pip install novita-client
