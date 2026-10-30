def onko_palindromi(mjono: str):
    for i in range(0, len(mjono) // 2):
        if mjono[i] != mjono[-1 - i]:
            return False
    return True

def poista_muut_kuin_kirjaimet(mjono):
    sallitut = "ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ"
    sallitut += sallitut.lower()
    
    tulos = ""
    for merkki in mjono:
        if merkki in sallitut:
            tulos += merkki
    
    return tulos

def ovatko_anagrammit(mjono1: str, mjono2: str):
    mjono1 = poista_muut_kuin_kirjaimet(mjono1)
    mjono2 = poista_muut_kuin_kirjaimet(mjono2)
    
    for kirjain in mjono1:
        if mjono1.count(kirjain) != mjono2.count(kirjain):
            return False
    
    return True

def laske_vokaalit(mjono):
    vok = "AEIOUYÅÄÖ"
    vok += vok.lower()

    vokaaleja = 0
    for merkki in mjono:
        if merkki in vok:
            vokaaleja += 1

    return vokaaleja

# TEST
print(ovatko_anagrammit("auto", "otu"))
