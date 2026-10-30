def lisaa_kirja(kirjailija: str, kirja: str, sivuja: int, julkaisuvuosi: int, kirjat: list):
    kirjat.append((kirjailija, kirja, sivuja, julkaisuvuosi))
    
def listaa_kirjat(kirjat: list, tulosta_indeksit=False):
    indeksi = 1
    for kirja in kirjat:
        if tulosta_indeksit:
            print(f"{indeksi}. ", end="")
            indeksi += 1
        print(f"{kirja[1]} ({kirja[3]}), {kirja[2]} s., kirjoittaja: {kirja[0]}")
        
def kirjoittajan_kirjat(kirjat: list, hakusana: str) -> list:
    lista = []
    for kirja in kirjat:
        if hakusana in kirja[0]:
            lista.append(kirja)
            
    return lista

def etsi_kirjat(kirjat: list, hakusana: str) -> list:
    lista = []
    for kirja in kirjat:
        if hakusana in kirja[1]:
            lista.append(kirja)
            
    return lista

def poista_kirja(kirjat: list, indeksi: int) -> tuple:
    return kirjat.pop(indeksi)
    
def tallenna_kirjat(kirjat: list):
    with open("kirjasto.dat", "w", encoding="utf-8") as tiedosto:
        for kirja in kirjat:
            s = f"{kirja[0]},{kirja[1]},{kirja[2]},{kirja[3]}\n"
            tiedosto.write(s)

def lue_kirjat() -> list:
    kirjat = []
    with open("kirjasto.dat", encoding="utf-8") as tiedosto:
        for rivi in tiedosto:
            data = rivi.split(",")
            kirja = (data[0], data[1], int(data[2]), int(data[3]))
            kirjat.append(kirja)
    return kirjat

    
def kysy_valinta() -> int:
    print("Valitse toiminta:")
    print("1. Lisää kirja")
    print("2. Poista kirja")
    print("3. Tulosta kirjat")
    print("4. Etsi kirjaa nimellä")
    print("5. Etsi kirjaa kirjailijan perusteella")
    print("0. Poistu")
    
    valinta = int(input("Anna valinta: "))
    print()
    return valinta

# Pääohjelma
kirjat = lue_kirjat()

while True:
    valinta = kysy_valinta()
    if valinta == 1:
        nimi = input("Anna nimi: ")
        kirjailija = input("Anna kirjailija: ")
        sivut = int(input("Anna sivumäärä: "))
        vuosi = int(input("Anna julkaisuvuosi: "))
        lisaa_kirja(kirjailija, nimi, sivut, vuosi, kirjat)
        print("Lisätty!")
    elif valinta == 2:
        listaa_kirjat(kirjat, True)
        poistettava = int(input("Mikä poistetaan? "))
        poista_kirja(kirjat, poistettava)
        print("Poistettu!")
    elif valinta == 3:
        listaa_kirjat(kirjat)
    elif valinta == 4:
        hakusana = input("Anna hakusana: ")
        listaa_kirjat(etsi_kirjat(kirjat, hakusana))
    elif valinta == 5:
        hakusana = input("Anna hakusana: ")
        listaa_kirjat(kirjoittajan_kirjat(kirjat, hakusana))
    elif valinta == 0:
        break
    
# Lopuksi tallennetaan    
tallenna_kirjat(kirjat)
