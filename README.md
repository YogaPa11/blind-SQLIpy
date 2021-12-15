# blind SQLIpy
Alat blind SQLIpy ini merupakan alat injeksi sql yang menggunakan metode time based blind sql injection metode tersebut membutuhkan waktu yang lama agar bisa mendapatkan sebuah server database. Alat yang saya bangun ini menggunakan bantuan sebuah library seperti library blinder dan requests untuk bisa mendapatkan server database tersebut dan bahasa pemrograman python.

# Yang Bisa Di Lakukan blind SQLIpy
1. Cek Injeksi URL Sasaran
2. Dapatkan Nama Database Sasaran
3. Dapatkan Nama Tabel Sasaran
4. Dapatkan Jumlah Tabel Sasaran
5. Dork Injeksi SQL

# Di Uji Pada :
- Windows
- Kali Linux

# Penginstallan Pada Windows Dan Kali Linux
```
https://github.com/galihap76/blind-SQLIpy.git
```
Kamu cukup clone dan simpan pada direktori mana pun.

# Penggunaan Pada Windows
```
C:\Users\GalihAp76>cd blind-SQLIpy
C:\Users\GalihAp76\blind-SQLIpy>sqli.py
```

# Penggunaan Pada Kali Linux
```
cd blind-SQLIpy
python3 sqli.py
```

# Penyerangan blind SQLIpy
```
 _     _ _           _   ____   ___  _     ___
| |__ | (_)_ __   __| | / ___| / _ \| |   |_ _|_ __  _   _
| '_ \| | | '_ \ / _` | \___ \| | | | |    | || '_ \| | | |
| |_) | | | | | | (_| |  ___) | |_| | |___ | || |_) | |_| |
|_.__/|_|_|_| |_|\__,_| |____/ \__\_\_____|___| .__/ \__, |
                                              |_|    |___/


 [>] Di Koding Oleh : Galih Anggoro Prasetya
 [>] Github         : https://github.com/galihap76




===================================
[+]         blind SQLIpy        [+]
===================================
 [1] CEK INJEKSI URL SASARAN
 [2] DAPATKAN NAMA DATABASE SASARAN
 [3] DAPATKAN NAMA TABEL SASARAN
 [4] DAPATKAN JUMLAH TABEL SASARAN
 [5] DORK INJEKSI SQL
 [6] INFO DAN CONTOH PENYERANGAN
 [7] KELUAR

===================================


[+] pilih nomor yang kamu mau : 2
[+] masukkan URL sasaran pada blind SQLIpy : http://testphp.vulnweb.com/product.php?pic=1
[!] harap tunggu...
[+] nama database pada sasaran :  acuart


[+] pilih nomor yang kamu mau :
```
Penyerangan blind SQLIpy pada nomor 2 untuk mendapatkan nama database sasaran.

# Pemberitahuan Dari Saya
Jika kamu menggunakan alat saya ini harap bersabar dan menunggu untuk mendapatkan server database sasaran karena ini menggunakan metode time based blind sql injection jadi ini juga membutuhkan koneksi internet.
