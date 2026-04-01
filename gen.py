import json
import random

prefixes = [
    "Analizza", "Spiega", "Descrivi", "Illustra", "Discuti", "Esamina", "Valuta", "Confronta", "Delinea", "Argomenta",
    "Chiarisci", "Approfondisci", "Dettaglia", "Riassumi", "Sintetizza", "Pondera", "Considera", "Dimostra", "Evidenzia", "Esponi"
]

subjects = [
    "i vantaggi dell'architettura Transformer",
    "i benefici tecnici dei Transformer",
    "la superiorità dei Transformer",
    "i punti di forza dei Transformer",
    "le innovazioni introdotte dai Transformer",
    "i miglioramenti dei Transformer",
    "i pro dell'architettura Transformer",
    "l'efficienza dei Transformer",
    "le caratteristiche vincenti dei Transformer",
    "il salto di qualità dei Transformer"
]

comparisons = [
    "rispetto alle classiche RNN.",
    "confrontandoli con le Recurrent Neural Networks.",
    "in contrapposizione alle RNN tradizionali.",
    "rispetto alle reti neurali ricorrenti standard.",
    "contro le architetture RNN storiche.",
    "superando i limiti delle RNN.",
    "in confronto ai modelli RNN.",
    "al posto delle classiche reti RNN.",
    "rispetto ai vecchi modelli ricorrenti.",
    "valutando i difetti delle RNN."
]

contexts = [
    "",
    " Considera in particolare la parallelizzazione.",
    " Fai riferimento al meccanismo di attention.",
    " Concentrati sul problema del vanishing gradient.",
    " Analizza la gestione delle dipendenze a lungo termine.",
    " Soffermati sull'efficienza computazionale.",
    " Tieni conto dell'addestramento su GPU.",
    " Valuta l'impatto del Multi-Head Attention.",
    " Spiega il ruolo del Positional Encoding.",
    " Dettaglia la complessità algoritmica."
]

outputs_intro = [
    "L'architettura Transformer, introdotta nel 2017 da Vaswani et al., ha rivoluzionato il campo del Machine Learning superando le classiche Reti Neurali Ricorrenti (RNN). ",
    "Il successo dei Transformer sulle RNN classiche deriva da un profondo cambio di paradigma architetturale. ",
    "Rispetto alle RNN, che elaborano i dati sequenzialmente, i Transformer offrono una serie di vantaggi strutturali e algoritmici. ",
    "L'adozione massiva dei Transformer al posto delle RNN tradizionali è giustificata da differenze tecniche cruciali. ",
    "Le differenze tra Transformer e RNN evidenziano il netto vantaggio della prima architettura, soprattutto nel NLP. "
]

outputs_points = [
    "In primis, l'elaborazione parallela: le RNN richiedono un'elaborazione sequenziale O(N), un limite per l'addestramento. I Transformer processano l'intera sequenza simultaneamente (O(1) operazioni sequenziali), sfruttando a pieno l'architettura SIMD delle moderne GPU e TPU. ",
    "Un aspetto fondamentale è la gestione delle dipendenze a lungo termine. Le RNN soffrono di vanishing gradient su sequenze lunghe. I Transformer usano la Self-Attention, connettendo direttamente ogni token con tutti gli altri, creando un percorso di lunghezza O(1) per il flusso delle informazioni. ",
    "La complessità computazionale varia. Per le RNN è O(N * D^2), per i Transformer i layer di Self-Attention sono O(N^2 * D). Quando la lunghezza N è minore della dimensionalità D, i Transformer risultano computazionalmente più efficienti. ",
    "Il Multi-Head Attention permette ai Transformer di prestare attenzione a diversi sottospazi di rappresentazione simultaneamente. Nelle RNN, l'hidden state deve condensare tutta l'informazione in un unico vettore, limitando la capacità di catturare sfaccettature multiple. ",
    "I Transformer introducono il Positional Encoding, iniettando informazioni sull'ordine dei token negli embedding. Ciò bypassa l'elaborazione step-by-step delle RNN, mantenendo la sequenzialità ma eliminando la latenza associata all'unrolling della rete. ",
    "A livello di accesso alla memoria, i Transformer operano tramite ampie moltiplicazioni di matrici ottimizzate (GEMM), con elevata località spaziale. Le RNN comportano continui accessi in memoria per aggiornare gli hidden state (memory-bound). "
]

outputs_conclusion = [
    "In sintesi, combinando attention globale ed elevata parallelizzazione, i Transformer risolvono i colli di bottiglia delle RNN.",
    "Complessivamente, l'eliminazione della ricorrenza ha permesso di addestrare modelli molto più grandi, impraticabile con le RNN.",
    "Per queste ragioni, l'architettura Transformer è oggi lo standard de facto, sostituendo quasi interamente le classiche RNN.",
    "Questi fattori rendono i Transformer esponenzialmente più scalabili, garantendo prestazioni superiori in training e inferenza.",
    "In conclusione, la capacità dei Transformer di gestire contesti ampi sancisce il loro netto vantaggio sulle RNN."
]

random.seed(42)

generated_instructions = set()
lines = []

while len(lines) < 200:
    prefix = random.choice(prefixes)
    subject = random.choice(subjects)
    comp = random.choice(comparisons)
    context = random.choice(contexts)

    instruction = f"{prefix} {subject} {comp}{context}"

    if instruction in generated_instructions:
        continue
    generated_instructions.add(instruction)

    intro = random.choice(outputs_intro)

    num_points = random.randint(3, 5)
    points = random.sample(outputs_points, num_points)

    conc = random.choice(outputs_conclusion)

    output = intro + "".join(points) + conc

    lines.append(json.dumps({"instruction": instruction, "output": output}, ensure_ascii=False))

with open("dataset_completo.jsonl", "a", encoding="utf-8") as f:
    for line in lines:
        f.write(line + "\n")

print("Done generating 200 lines.")
