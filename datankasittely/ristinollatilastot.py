def kysy_valinta() -> int:
    print("Valitse seuraavista:")
    print("1. Lisää siirto")
    print("2. Poista siirto")
    print("3. Tulosta kaikki siirrot")
    print("0. Lopeta")

    while True:
        try:
            valinta = int(input("Anna valinta: "))
            if valinta in (0,1,2,3):
                return valinta
            print("Virheellinen valinta!")
        except:
            print("Anna numero!")


def lisaa_siirto(siirrot: list):
    # merkki
    while True:
        merkki = input("Anna merkki (o/x): ").lower()
        if merkki in ("o","x"):
            break
        print("Virhe: käytä vain O tai X.")

    # koordinaatit
    while True:
        try:
            x = int(input("Anna x: "))
            y = int(input("Anna y: "))

            if x not in (0,1,2) or y not in (0,1,2):
                print("Koordinaattien tulee olla välillä 0–2.")
                continue

            # ruutu varattu?
            for s in siirrot:
                if s[1] == x and s[2] == y:
                    print("Ruutu on jo varattu!")
                    raise ValueError
            break
        except ValueError:
            print("Anna kelvolliset koordinaatit!")

    siirrot.append((merkki, x, y))


def poista_siirto(siirrot: list):
    if not siirrot:
        print("Ei siirtoja poistettavaksi.")
        return

    for i, s in enumerate(siirrot):
        print(f"{i}: {s}")

    while True:
        try:
            poistettava = int(input("Mikä poistetaan? "))
            if 0 <= poistettava < len(siirrot):
                poistettu = siirrot.pop(poistettava)
                print(f"Poistettiin {poistettu}")
                return
            print("Virheellinen numero!")
        except:
            print("Anna numero!")


def tulosta_siirrot(siirrot: list):
    for s in siirrot:
        print(s)


# --- PÄÄOHJELMA ---
siirrot = []

while True:
    valinta = kysy_valinta()

    if valinta == 1:
        lisaa_siirto(siirrot)
    elif valinta == 2:
        poista_siirto(siirrot)
    elif valinta == 3:
        tulosta_siirrot(siirrot)
    elif valinta == 0:
        break