# Python-harjoituksia

Kokoelma Turun yliopiston *Ohjelmoinnin perusteet* -kurssin (syksy 2025) ohjelmia, jotka käsittelevät tiedostoja, dataa ja käyttöliittymiä.

## Sisältö

### `kirjasto/` – kirjojen hallintaohjelma
- `kirjasto.py`: komentoriviohjelma kirjojen lisäämiseen, hakemiseen, listaamiseen ja poistamiseen. Tiedot tallentuvat tiedostoon `kirjasto.dat`.
- `kirjasto_gui.py`: sama logiikka graafisella **Tkinter**-käyttöliittymällä.

```bash
cd kirjasto
python kirjasto_gui.py
```

### `datankasittely/` – datan siivous ja analyysi
- `korjaa_vuodet.py`: lukee virheellistä vuosiväliaineistoa (`vuodet.dat`), hylkää virheelliset rivit, korjaa väärin päin olevat välit ja kirjoittaa siistityn tiedoston.
- `prosessoi_nimet.py`: lukee nimilistan, ohittaa puutteelliset rivit, järjestää nimet ja tallentaa ne. Kattava virheenkäsittely (puuttuva tiedosto, käyttöoikeudet, ylikirjoituksen vahvistus).
- `ristinollatilastot.py`: valikkopohjainen ohjelma ristinollan siirtojen kirjaamiseen ja tarkasteluun syötteiden validoinnilla.

### `merkkijonot/` – merkkijonofunktiot
- `sana_apuri.py`: palindromi- ja anagrammitarkistus sekä vokaalien laskeminen.

## Teknologiat

Python 3, Tkinter, tiedostojen luku ja kirjoitus, virheenkäsittely

## Tekijä

Tomas Salo
