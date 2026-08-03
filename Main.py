import subprocess
import os
import sys

def pokreni_skriptu(ime_skripte):
    """Pomoćna funkcija za pokretanje pojedine skripte i praćenje grešaka."""
    print(f"\n[POKRETANJE] {ime_skripte}...")
    print("-" * 50)
    
    # Pokrećemo skriptu koristeći trenutni Python interpreter
    rezultat = subprocess.run([sys.executable, ime_skripte])
    
    if rezultat.returncode == 0:
        print(f"[USPJEH] {ime_skripte} je uspješno izvršena.")
    else:
        print(f"[GREŠKA] Došlo je do problema prilikom izvršavanja {ime_skripte}.")
        # Prekidamo izvršavanje main.py ako neka od ključnih skripti javi grešku
        sys.exit(1)

def main():
    print("=" * 60)
    print("     POKRETANJE ANALIZE")
    print("=" * 60)

    # Nabava i priprema podataka (Ovo je ključno za sve ostale korake!)
    pokreni_skriptu("Nabava_podataka.py")
    
    # Pregled strukture i izračun osnovne statistike
    pokreni_skriptu("Struktura_podataka.py")
    pokreni_skriptu("Izračun_statistike.py")
    pokreni_skriptu("Kumulativni_prikaz.py")
    # Izračun i vizualizacija povrata te volatilnosti
    pokreni_skriptu("Računanje_prinosa.py")
    pokreni_skriptu("Računanje_volatilnosti.py")
    pokreni_skriptu("Rolling_volatilnost_i_prikaz.py")
    
    # Tehnička analiza i indikatori
    pokreni_skriptu("Jednostavni_pokretni_prosjeci.py")
    pokreni_skriptu("EMA_indikator.py")
    pokreni_skriptu("RSI.py")
    pokreni_skriptu("MACD_indikator.py")
    pokreni_skriptu("Bollingerove_trake.py")
    
    # Napredne vizualizacije (Korelacija, Sezonalnost, Histogram)
    pokreni_skriptu("Korelacijska_matrica.py")
    pokreni_skriptu("Analiza_sezonalnosti.py")
    pokreni_skriptu("Histogram_dnevnih_prinosa.py")
    # Spremanje u excel izvještaj
    pokreni_skriptu("Izvoz_excel.py")

    print("\n" + "=" * 60)
    print(" [ZAVRŠENO] Cijela skripta je uspješno izvršena!")
    print("=" * 60)

if __name__ == "__main__":
    main()
