from datetime import datetime

NYKYINEN = datetime.now().year


def korjaa_rivi(rivi: str):
  
    rivi = rivi.strip()


    if not rivi:
        return None


    osat = rivi.split("-")
    if len(osat) != 2:
        return None

    try:
        alku = int(osat[0])
        loppu = int(osat[1])
    except ValueError:
        return None


    if not (0 <= alku <= NYKYINEN):
        return None

    if not (0 <= loppu <= NYKYINEN):
        return None

   
    if loppu < alku:
        alku, loppu = loppu, alku

    return f"{alku}-{loppu}"


def main():
   
    with open("vuodet.dat", "r", encoding="utf-8") as infile, \
         open("korjatut_vuodet.dat", "w", encoding="utf-8") as outfile:

        for rivi in infile:
            korjattu = korjaa_rivi(rivi)
            if korjattu is not None:
                outfile.write(korjattu + "\n")


if __name__ == "__main__":
    main()
