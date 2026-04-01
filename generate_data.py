import json
import itertools

def generate_dataset():
    prefixes = [
        "Potresti spiegarmi come ",
        "Vorrei sapere come ",
        "Qual è il modo migliore per ",
        "Dimmi come ",
        "Hai idea di come ",
        "Sapresti dirmi come ",
        "Puoi aiutarmi a ",
        "Mi spiegheresti come ",
        "Scrivi le istruzioni per ",
        "Fornisci una guida su come "
    ]

    cores = [
        "scrivere un'espressione regolare complessa per estrarre indirizzi email validi da un testo non strutturato",
        "creare una regex avanzata per individuare email valide in testi liberi",
        "costruire un'espressione regolare robusta per il parsing di indirizzi email da stringhe generiche",
        "formulare una regex dettagliata per isolare email corrette da documenti di testo",
        "sviluppare un pattern regex complesso per catturare indirizzi email da testo grezzo",
        "realizzare un'espressione regolare che trovi indirizzi di posta elettronica all'interno di un testo disordinato"
    ]

    suffixes = [
        "?",
        " in modo dettagliato.",
        " passo dopo passo.",
        " con esempi esplicativi.",
        " considerando vari casi limite."
    ]

    instructions = []
    for p, c, s in itertools.product(prefixes, cores, suffixes):
        instruction = p + c + s
        instructions.append(instruction)

    # We only need 200
    instructions = instructions[:200]

    base_output = (
        "Per estrarre indirizzi email validi da un testo non strutturato, è necessario utilizzare un'espressione regolare (regex) "
        "robusta che tenga conto delle specifiche RFC 5322, pur mantenendo un livello di complessità gestibile. "
        "L'espressione regolare che ti propongo è la seguente: "
        r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\]) "
        "Analizziamo la struttura di questa regex parte per parte. "
        "La parte locale (prima del simbolo chiocciola) è gestita da: "
        r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\") "
        "Questa sezione permette lettere minuscole, numeri e una serie di caratteri speciali definiti nello standard, oltre a consentire "
        "l'uso di stringhe tra virgolette che possono contenere spazi e altri caratteri. Inoltre, garantisce che i punti non siano né "
        "all'inizio, né alla fine, né consecutivi nella parte locale senza virgolette. "
        "Il simbolo chiocciola @ separa la parte locale dal dominio. "
        "La parte del dominio è gestita da: "
        r"(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\]) "
        "Questa sezione convalida due formati principali per il dominio: i nomi di dominio tradizionali e gli indirizzi IP (IPv4 e IPv6) tra parentesi quadre. "
        "Per i nomi di dominio, la regex si assicura che ogni etichetta (separata da un punto) inizi e finisca con una lettera o un numero e possa contenere trattini intermedi. "
        "Per gli indirizzi IP, verifica la correttezza strutturale, ad esempio che i numeri per l'IPv4 siano compresi tra 0 e 255 e separati correttamente dai punti. "
        "Utilizzando un motore regex moderno compatibile con PCRE, questa espressione è in grado di estrarre in modo affidabile gli indirizzi email "
        "ignorando il testo circostante. Se si utilizza in Python, è raccomandato impiegare il modulo 're' con re.IGNORECASE per supportare l'estrazione case-insensitive, "
        "oppure estendere la regex includendo le lettere maiuscole [A-Za-z0-9...]."
    )

    with open("dataset_completo.jsonl", "a", encoding="utf-8") as f:
        for i, instruction in enumerate(instructions):
            # To add slightly more variation if needed, but not strictly required
            output = base_output
            record = {
                "instruction": instruction,
                "output": output
            }
            f.write(json.dumps(record, ensure_ascii=False) + "\n")

if __name__ == "__main__":
    generate_dataset()
