import time

def hitung_panjang(nama):
    return len(nama)

def balik_kata(nama):
    return ' '.join(nama.split()[::-1])

def format_kapital(nama):
    return nama.upper()

def buat_inisial(nama):
   kata_kata = nama.split()
    inisial = "".join([k[0].upper() for k in kata_kata])
    return inisial

def convert_to_leetspeak(nama):
   pengganti = {'a': '4', 'e': '3', 'i': '1', 'o': '0', 's': '5', 'g': '6', 't': '7'}
    nama_lower = nama.lower()
    hasil = ""
    for huruf in nama_lower:
      hasil += pengganti.get(huruf, huruf) 
    return hasil.upper()

def cek_palindrom(nama):
    nama_bersih = nama.replace(" ", "").lower()
    return "YA" if nama_bersih == nama_bersih[::-1] else "TIDAK"

def main():
    print("==========================================")
    print("      THE IDENTITY TOOLKIT v.2.0          ")
    print("==========================================")
    
    nama_input = input(">> Masukkan Nama Lengkap Anda: ").strip()

    if not nama_input:
        print("Error: Nama tidak boleh kosong!")
        return

    print("\nSedang menganalisis data...", end="")
    for _ in range(3):
        time.sleep(0.5) 
        print(".", end="", flush=True)
    print("\n")

   panjang = hitung_panjang(nama_input)
    terbalik = balik_kata(nama_input)
    kapital = format_kapital(nama_input)
    inisial = buat_inisial(nama_input)
    hacker_mode = convert_to_leetspeak(nama_input)
    is_palindrom = cek_palindrom(nama_input)

    print(f"[-] Panjang Karakter  : {panjang} char")
    print(f"[-] Format Kapital    : {kapital}")
    print(f"[-] Susunan Terbalik  : {terbalik}")
    print(f"[-] Kode Inisial      : {inisial}")
    print(f"[-] Status Palindrom  : {is_palindrom}")
    print("-" * 42)
    print(f"[+] HACKER MODE ID    : {hacker_mode}")
    print("==========================================")

if __name__ == "__main__":
    main()
