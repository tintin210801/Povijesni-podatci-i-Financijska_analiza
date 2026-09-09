import subprocess
import os
import sys
from concurrent.futures import ProcessPoolExecutor, as_completed

def pokreni_skriptu(ime_skripte):
    """Pomoćna funkcija za pokretanje pojedine skripte i praćenje grešaka."""
    print(f"\n[POKRETANJE] {ime_skripte}...")
    rezultat = subprocess.run([sys.executable, ime_skripte])
    
    if rezultat.returncode == 0:
        print(f"[USPJEH] {ime_skripte} je uspješno izvršena.")
        return True
    else:
        print(f"[GREŠKA] Došlo je do problema prilikom izvršavanja {ime_skripte}.")
        return False

def main():
    os.environ["MPLBACKEND"] = "Agg"

    print("=" * 60)
    print("      POKRETANJE ANALIZE (OPTIMIZIRANO)")
    print("=" * 60)

    # 1. Korak: Sekvencijalno (Ovo je preduvjet za sve ostalo)
    osnovne_skripte = [
        "Nabava_podataka.py",
        "Struktura_podataka.py",
        "Izračun_statistike.py"
    ]
    
    for skripta in osnovne_skripte:
        if not pokreni_skriptu(skripta):
            sys.exit(1)

    # 2. Korak: Paralelno (Skripte koje mogu raditi istovremeno)
    paralelne_skripte = [
        "Kumulativni_prikaz.py",
        "Računanje_prinosa.py",
        "Računanje_volatilnosti.py",
        "Rolling_volatilnost_i_prikaz.py",
        "Jednostavni_pokretni_prosjeci.py",
        "EMA_indikator.py",
        "RSI.py",
        "MACD_indikator.py",
        "Bollingerove_trake.py",
        "Korelacijska_matrica.py",
        "Analiza_sezonalnosti.py",
        "Histogram_dnevnih_prinosa.py",
        "Info.py"
    ]

    print(f"\n[INFO] Pokretanje {len(paralelne_skripte)} skripti paralelno...")
    
    with ProcessPoolExecutor() as executor:
        futures = {executor.submit(pokreni_skriptu, s): s for s in paralelne_skripte}
        for future in as_completed(futures):
            if not future.result():
                print(f"[GREŠKA] Jedna od paralelnih skripti je pala.")
                sys.exit(1)

    # 3. Korak: Završni izvoz (čeka da sve paralelne završe)
    if not pokreni_skriptu("Izvoz_excel.py"):
        sys.exit(1)

    print("\n" + "=" * 60)
    print(" [ZAVRŠENO] Cijela skripta je uspješno i ubrzano izvršena!")
    print("=" * 60)

if __name__ == "__main__":
    main()