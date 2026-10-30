import os
import sys

def lue_tiedosto(tiedostonimi):
    """Lukee tiedoston ja palauttaa rivit listana. Käsittelee virheet."""
    if not os.path.exists(tiedostonimi):
        print(f"Virhe: Tiedostoa '{tiedostonimi}' ei löydy.")
        return None

    try:
        # encoding='utf-8' on tärkeä ääkkösten kannalta
        with open(tiedostonimi, 'r', encoding='utf-8') as tiedosto:
            return tiedosto.readlines()
    except PermissionError:
        print(f"Virhe: Sinulla ei ole oikeuksia lukea tiedostoa '{tiedostonimi}'.")
    except Exception as e:
        print(f"Odottamaton virhe tiedostoa luettaessa: {e}")
    
    return None

def muotoile_ja_jarjesta(nimilista):
    """Muuttaa nimet muotoon 'Sukunimi, Etunimi' ja järjestää ne."""
    muotoillut_nimet = []
    
    for rivi in nimilista:
        rivi = rivi.strip()
        if not rivi: # Ohitetaan tyhjät rivit
            continue
            
        osat = rivi.split(" ", 1) # Splitataan vain ensimmäisestä välistä
        
        if len(osat) < 2:
            print(f"Varoitus: Rivillä '{rivi}' ei ole selkeää etu- ja sukunimeä. Ohitetaan.")
            continue
            
        etunimi = osat[0]
        sukunimi = osat[1]
        muotoillut_nimet.append(f"{sukunimi}, {etunimi}")
    
    muotoillut_nimet.sort()
    return muotoillut_nimet

def tallenna_tiedosto(tiedostonimi, data):
    """Kirjoittaa datan tiedostoon. Varmistaa, ettei ylikirjoiteta vahingossa."""
    
    # Tietoturva/Käytettävyys: Estetään vahinkoylikirjoitus
    if os.path.exists(tiedostonimi):
        vastaus = input(f"Tiedosto '{tiedostonimi}' on jo olemassa. Ylikirjoitetaanko? (k/e): ")
        if vastaus.lower() != 'k':
            print("Toiminto peruttu. Tiedostoa ei tallennettu.")
            return False

    try:
        with open(tiedostonimi, "w", encoding='utf-8') as tiedosto:
            for rivi in data:
                tiedosto.write(rivi + "\n")
        print(f"Tiedot tallennettu onnistuneesti tiedostoon '{tiedostonimi}'.")
        return True
    except PermissionError:
        print(f"Virhe: Sinulla ei ole oikeuksia kirjoittaa tiedostoon '{tiedostonimi}'.")
    except OSError as e:
        print(f"Levyvirhe tai muu käyttöjärjestelmän virhe: {e}")
        
    return False

def main():
    # 1. Tiedoston luku
    luku_nimi = input("Anna luettavan tiedoston nimi: ")
    raaka_data = lue_tiedosto(luku_nimi)
    
    if raaka_data is None:
        return # Lopetetaan, jos luku epäonnistui

    # 2. Datan käsittely
    valmiit_nimet = muotoile_ja_jarjesta(raaka_data)
    
    if not valmiit_nimet:
        print("Ei käsiteltäviä nimiä.")
        return

    # 3. Tiedoston tallennus
    kohde_nimi = input("Anna kohdetiedoston nimi: ")
    
    # Estetään lukutiedoston ylikirjoittaminen samalla nimellä ilman varoitusta
    if kohde_nimi == luku_nimi:
        print("Varoitus: Yrität tallentaa samalla nimellä kuin lähdetiedosto.")
    
    tallenna_tiedosto(kohde_nimi, valmiit_nimet)

if __name__ == "__main__":
    main()