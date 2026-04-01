import json

prefixes = [
    "Spiega", "Illustra", "Descrivi", "Analizza", "Chiarisci",
    "Dettaglia", "Fornisci una spiegazione su", "Fornisci un'analisi di",
    "Esponi", "Riassumi in dettaglio"
]

middles = [
    "il funzionamento", "il meccanismo", "l'architettura",
    "i principi matematici", "l'implementazione", "le basi teoriche",
    "la logica alla base", "i concetti fondamentali"
]

suffixes = [
    "del meccanismo di RoPE (Rotary Position Embedding).",
    "dei Rotary Position Embeddings (RoPE).",
    "del RoPE nei Transformers.",
    "degli embedding posizionali rotazionali (RoPE).",
    "del sistema RoPE utilizzato nei Large Language Models.",
    "del metodo Rotary Position Embedding."
]

output_base = "Il Rotary Position Embedding (RoPE) è un metodo avanzato per iniettare informazioni posizionali nei modelli basati su architettura Transformer. A differenza degli embedding posizionali assoluti (come quelli sinusoidali originali di Vaswani et al.) o relativi tradizionali, RoPE codifica la posizione assoluta con una matrice di rotazione e, di conseguenza, incorpora la posizione relativa direttamente nel calcolo dell'attenzione (dot-product).\n\nDal punto di vista matematico, RoPE mappa i vettori delle query (q) e delle key (k) in uno spazio vettoriale complesso. Per un vettore di dimensione d (che deve essere pari), lo spazio viene diviso in d/2 sottospazi bidimensionali. A ciascuna di queste coppie (x_{2i}, x_{2i+1}) viene applicata una rotazione di un angolo proporzionale alla posizione assoluta 'm' del token, calcolato come m * theta_i, dove theta_i = 10000^{-2i/d}. Questa rotazione nel piano bidimensionale si ottiene moltiplicando il vettore per una matrice di rotazione 2x2.\n\nL'eleganza di questo approccio si manifesta nel meccanismo di attention: quando si calcola il prodotto scalare tra una query alla posizione 'm' e una key alla posizione 'n', la proprietà delle rotazioni fa sì che il risultato dipenda solo dalla differenza di posizione (m - n). Infatti, <R_m q, R_n k> = <q, R_{m-n} k>. Questo permette al modello di catturare le dipendenze relative in modo naturale, mantenendo al contempo le informazioni sulla posizione assoluta.\n\nInoltre, RoPE offre vantaggi significativi in termini di estrapolazione della lunghezza del contesto. Poiché il modello apprende a focalizzarsi sulle distanze relative attraverso rotazioni matematicamente coerenti, si comporta in modo più robusto quando deve gestire sequenze più lunghe rispetto a quelle viste in fase di addestramento. Implementativamente, per efficienza computazionale, la rotazione non avviene tramite moltiplicazione di matrici sparse, ma applicando trasformazioni elementari sfruttando le proprietà dei numeri complessi o operazioni vettorializzate elementari (es. applicando funzioni seno e coseno punto a punto sui vettori trasformati)."

instructions = []
for p in prefixes:
    for m in middles:
        for s in suffixes:
            instructions.append(f"{p} {m} {s}")

with open("dataset_completo.jsonl", "a", encoding="utf-8") as f:
    for i in range(200):
        # We take the first 200 unique instructions
        instruction = instructions[i]

        # We can add a small dynamic part to the output to make them slightly unique if desired,
        # but the prompt says 'basate su questo argomento'.
        # We will keep the output text identical and highly detailed as requested.

        record = {
            "instruction": instruction,
            "output": output_base
        }

        # Write exactly as json string with no pretty-print, to be a single line per record
        f.write(json.dumps(record, ensure_ascii=False) + "\n")

print("Generated 200 lines in dataset_completo.jsonl")
