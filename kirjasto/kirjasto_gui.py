import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import ttk

# ====== LOGIIKKA SAMA KUIN ALKUPERÄISESSÄ OHJELMASSA ======

def lisaa_kirja(kirjailija: str, kirja: str, sivuja: int, julkaisuvuosi: int, kirjat: list):
    kirjat.append((kirjailija, kirja, sivuja, julkaisuvuosi))
    
def listaa_kirjat(kirjat: list):
    return [f"{kirja[1]} ({kirja[3]}), {kirja[2]} s., kirjoittaja: {kirja[0]}" for kirja in kirjat]

def kirjoittajan_kirjat(kirjat: list, hakusana: str) -> list:
    return [kirja for kirja in kirjat if hakusana.lower() in kirja[0].lower()]

def etsi_kirjat(kirjat: list, hakusana: str) -> list:
    return [kirja for kirja in kirjat if hakusana.lower() in kirja[1].lower()]

def poista_kirja(kirjat: list, indeksi: int):
    return kirjat.pop(indeksi)

def tallenna_kirjat(kirjat: list):
    with open("kirjasto.dat", "w", encoding="utf-8") as tiedosto:
        for kirja in kirjat:
            s = f"{kirja[0]},{kirja[1]},{kirja[2]},{kirja[3]}\n"
            tiedosto.write(s)

def lue_kirjat() -> list:
    kirjat = []
    try:
        with open("kirjasto.dat", encoding="utf-8") as tiedosto:
            for rivi in tiedosto:
                data = rivi.strip().split(",")
                if len(data) != 4:
                    continue
                kirja = (data[0], data[1], int(data[2]), int(data[3]))
                kirjat.append(kirja)
    except FileNotFoundError:
        pass
    return kirjat


# ====== TKINTER-GUI ======

class KirjastoGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Kirjasto – Tkinter GUI")

        self.kirjat = lue_kirjat()

        # Kirjalista (Listbox)
        self.lista = tk.Listbox(root, width=60, height=15)
        self.lista.pack(pady=10)

        # Painikkeet
        frame = tk.Frame(root)
        frame.pack()

        tk.Button(frame, text="Lisää kirja", command=self.lisaa_kirja_gui).grid(row=0, column=0, padx=5)
        tk.Button(frame, text="Poista kirja", command=self.poista_kirja_gui).grid(row=0, column=1, padx=5)
        tk.Button(frame, text="Etsi nimellä", command=self.hae_nimella).grid(row=0, column=2, padx=5)
        tk.Button(frame, text="Etsi kirjailijalla", command=self.hae_kirjailijalla).grid(row=0, column=3, padx=5)
        tk.Button(frame, text="Näytä kaikki", command=self.paivita_lista).grid(row=0, column=4, padx=5)

        self.paivita_lista()

        # Ikkunan sulkeminen
        self.root.protocol("WM_DELETE_WINDOW", self.sulje)

    def paivita_lista(self, lista=None):
        self.lista.delete(0, tk.END)
        if lista is None:
            lista = self.kirjat
        for rivi in listaa_kirjat(lista):
            self.lista.insert(tk.END, rivi)

    def lisaa_kirja_gui(self):
        kirjailija = simpledialog.askstring("Kirjailija", "Anna kirjailija:")
        if not kirjailija:
            return

        nimi = simpledialog.askstring("Kirjan nimi", "Anna nimi:")
        if not nimi:
            return

        try:
            sivut = int(simpledialog.askstring("Sivumäärä", "Anna sivumäärä:"))
            vuosi = int(simpledialog.askstring("Julkaisuvuosi", "Anna julkaisuvuosi:"))
        except:
            messagebox.showerror("Virhe", "Sivumäärän ja vuoden pitää olla numeroita.")
            return

        lisaa_kirja(kirjailija, nimi, sivut, vuosi, self.kirjat)
        self.paivita_lista()

    def poista_kirja_gui(self):
        valinta = self.lista.curselection()
        if not valinta:
            messagebox.showwarning("Virhe", "Valitse poistettava kirja listasta.")
            return

        indeksi = valinta[0]
        poista_kirja(self.kirjat, indeksi)
        self.paivita_lista()

    def hae_nimella(self):
        hakusana = simpledialog.askstring("Haku", "Etsi kirjaa nimellä:")
        if not hakusana:
            return
        tulos = etsi_kirjat(self.kirjat, hakusana)
        self.paivita_lista(tulos)

    def hae_kirjailijalla(self):
        hakusana = simpledialog.askstring("Haku", "Etsi kirjailijan perusteella:")
        if not hakusana:
            return
        tulos = kirjoittajan_kirjat(self.kirjat, hakusana)
        self.paivita_lista(tulos)

    def sulje(self):
        tallenna_kirjat(self.kirjat)
        self.root.destroy()


# ====== PÄÄOHJELMA ======
if __name__ == "__main__":
    root = tk.Tk()
    gui = KirjastoGUI(root)
    root.mainloop()