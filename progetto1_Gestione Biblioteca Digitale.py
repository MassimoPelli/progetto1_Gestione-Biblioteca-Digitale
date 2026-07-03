# =====================================================================
#Progetto 1: Gestione Biblioteca Digitale
# =====================================================================

"""
Traccia In una biblioteca digitale si vuole realizzare un piccolo sistema software per gestire libri, utenti e prestiti.
Il programma deve sfruttare variabili, tipi di dati, strutture di controllo 
e soprattutto la programmazione orientata agli oggetti (OOP)"""

# =====================================================================
# PARTE 1 – Variabili e tipi di dati
# =====================================================================

"""Parte 1 Variabili e tipi di dati
Dichiarare e stampare alcune variabili di esempio:
Titolo di un libro (stringa)
Numero di copie disponibili (intero)
Prezzo medio di un libro (float)
Stato "disponibile/non disponibile" (booleano)(Esempio: titolo = "Il Signore degli Anelli", copie = 5, ecc.)"""

titolo = "Il Signore degli Anelli"
copie = 5
prezzo_medio = 15.99
disponibile = True  

print("--- Parte 1: Variabili e tipi di dati ---")
print(f"Titolo: {titolo}")
print(f"Copie disponibili: {copie}")
print(f"Prezzo medio: €{prezzo_medio}")
print(f"Disponibile: {disponibile}")
print("\n" + "="*40 + "\n")

# =====================================================================
# PARTE 2 – Strutture dati
# =====================================================================

"""Parte 2 Strutture dati
Creare una lista con almeno 5 titoli di libri.
Creare un dizionario che mappi il titolo del libro al numero di copie disponibili.
Creare un insieme (set) che contenga tutti gli utenti registrati alla biblioteca."""

catalogo_libri = [
    "Il Signore degli Anelli", 
    "1984", 
    "Il Piccolo Principe", 
    "Dune", 
    "Neuromante"
]

inventario_copie = {
    "Il Signore degli Anelli": 3,
    "1984": 2,
    "Il Piccolo Principe": 5,
    "Dune": 1,
    "Neuromante": 0  # Lo mettiamo a zero per testare poi il caso di errore nel prestito
}

utenti_registrati = {"Alice Rossi", "Bob Bianchi", "Charlie Verdi"}

print("--- Parte 2: Strutture dati iniziali ---")
print(f"Catalogo libri (Lista): {catalogo_libri}")
print(f"Inventario copie (Dizionario): {inventario_copie}")
print(f"Utenti registrati (Set): {utenti_registrati}")
print("\n" + "="*40 + "\n")

# =====================================================================
# PARTE 3 – Classi e OOP
# =====================================================================

"""Parte 3 Classi e OOP
Creare una classe Libro con attributi: titolo, autore, anno, copie_disponibili
Aggiungere un metodo info() che restituisca una stringa descrittiva del libro.
Creare una classe Utente con attributi: nome, eta, id_utente
Aggiungere un metodo scheda() che stampi i dati dell’utente.
Creare una classe Prestito che colleghi un Utente a un Libro e contenga:
utente (oggetto Utente), libro (oggetto Libro), giorni (numero di giorni del prestito)
Aggiungere un metodo dettagli() che stampi tutte le informazioni sul prestito."""

print("--- Parte 3: Classi e OOP ---")

class Libro:
    def __init__(self, titolo, autore, anno, copie_disponibili):
        self.titolo = titolo
        self.autore = autore
        self.anno = anno
        self.copie_disponibili = copie_disponibili

    def info(self):
        return f"Titolo: {self.titolo}, Autore: {self.autore}, Anno: {self.anno}, Copie disponibili: {self.copie_disponibili}"
    
class Utente:
    def __init__(self, nome, eta, id_utente):
        self.nome = nome
        self.eta = eta
        self.id_utente = id_utente

    def scheda(self):
        # La traccia chiede di STAMPARE, quindi usiamo print() direttamente qui
        print(f"Nome: {self.nome}, Età: {self.eta}, ID Utente: {self.id_utente}")
    
class Prestito:
    def __init__(self, utente, libro, giorni):
        self.utente = utente
        self.libro = libro
        self.giorni = giorni

    def dettagli(self):
        print(f"Prestito - Utente: {self.utente.nome}, Libro: {self.libro.titolo}, Giorni: {self.giorni}")
    
# =====================================================================
# PARTE 4 – Funzionalità e Simulazione
# =====================================================================

"""Parte 4 Funzionalità
Creare una funzione presta_libro(utente, libro, giorni) che:
Verifichi se il libro ha almeno 1 copia disponibile
Se sì → riduca il numero di copie e crei un nuovo oggetto Prestito
Se no → stampi un messaggio di errore
Simulare almeno 3 prestiti con utenti e libri diversi.
Stampare a video: L’elenco aggiornato delle copie disponibili per ciascun libro e i dettagli di ogni prestito effettuato """

def presta_libro(utente, libro, giorni):
    if libro.copie_disponibili > 0:
        libro.copie_disponibili -= 1
        nuovo_prestito = Prestito(utente, libro, giorni)
        nuovo_prestito.dettagli()  # Stampa i dettagli del prestito
        return nuovo_prestito
    else:
        print(f"Errore: Il libro '{libro.titolo}' non è disponibile per il prestito.")
        return None
    
# --- Creazione delle istanze (Libri e Utenti reali) ---
libro1 = Libro("Il Signore degli Anelli", "J.R.R. Tolkien", 1954, 3)
libro2 = Libro("1984", "George Orwell", 1949, 2)
libro3 = Libro("Neuromante", "William Gibson", 1984, 0) # Copie esaurite per il test

utente1 = Utente("Alice Rossi", 25, "U001")
utente2 = Utente("Bob Bianchi", 34, "U002")
utente3 = Utente("Charlie Verdi", 19, "U003")

# Lista per tenere traccia dei prestiti andati a buon fine
registro_prestiti = []

# --- Simulazione dei prestiti ---
prestito1 = presta_libro(utente1, libro1, 14)  # Prestito riuscito
if prestito1:
    registro_prestiti.append(prestito1)

prestito2 = presta_libro(utente2, libro2, 7)   # Prestito riuscito
if prestito2:
    registro_prestiti.append(prestito2)

prestito3 = presta_libro(utente3, libro3, 10)  # Prestito fallito (copie esaurite)
if prestito3:
    registro_prestiti.append(prestito3)

# --- Stampa dell'elenco aggiornato delle copie disponibili ---
print("\n--- Elenco aggiornato delle copie disponibili ---")
for libro in [libro1, libro2, libro3]:
    print(libro.info())

# --- Stampa dei dettagli di ogni prestito effettuato ---
print("\n--- Dettagli dei prestiti effettuati ---")
for prestito in registro_prestiti:
    prestito.dettagli()  # Ora stampa da solo, non serve il print() esterno!