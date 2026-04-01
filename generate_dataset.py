import json

def generate_data():
    prefixes = [
        "Fornisci un esempio pratico di utilizzo della libreria Hugging Face Transformers per la tokenizzazione.",
        "Mostrami come usare la libreria Hugging Face Transformers per tokenizzare del testo.",
        "Scrivi un esempio di tokenizzazione con Hugging Face Transformers.",
        "Spiega come effettuare la tokenizzazione utilizzando Hugging Face Transformers con un esempio.",
        "Fammi un esempio concreto di tokenizzazione con la libreria Transformers di Hugging Face.",
        "Puoi mostrare un esempio pratico di tokenizzazione usando Hugging Face?",
        "Dammi un esempio pratico per tokenizzare una stringa con Hugging Face Transformers.",
        "Illustra il processo di tokenizzazione con Hugging Face attraverso un esempio pratico.",
        "Come si usa la libreria Hugging Face per tokenizzare? Fai un esempio pratico.",
        "Vorrei un esempio pratico di utilizzo di Hugging Face Transformers per la tokenizzazione."
    ]

    models = [
        "bert-base-uncased", "roberta-base", "gpt2", "t5-small", "facebook/bart-base",
        "distilbert-base-uncased", "albert-base-v2", "google/electra-small-discriminator",
        "microsoft/deberta-base", "xlnet-base-cased", "google/mobilebert-uncased",
        "camembert-base", "flaubert/flaubert_base_uncased", "allenai/longformer-base-4096",
        "google/bigbird-roberta-base", "xlm-roberta-base", "Helsinki-NLP/opus-mt-en-it",
        "google/pegasus-xsum", "facebook/mbart-large-cc25", "EleutherAI/gpt-neo-125M"
    ]

    dataset = []
    for prefix in prefixes:
        for model in models:
            instruction = f"{prefix} Puoi fare riferimento al modello {model}."

            output = f"Certamente. Ecco una spiegazione tecnica dettagliata su come effettuare la tokenizzazione con Hugging Face Transformers utilizzando il modello {model}. Innanzitutto, è necessario assicurarsi che la libreria transformers sia installata nel proprio ambiente Python. Il modo più semplice e consigliato per istanziare un tokenizzatore è usare la classe AutoTokenizer, che caricherà automaticamente la configurazione corretta per {model}. Nel tuo script Python, dovrai importare la classe: from transformers import AutoTokenizer. Fatto ciò, puoi istanziare il tokenizzatore chiamando il metodo from_pretrained: tokenizer = AutoTokenizer.from_pretrained('{model}'). A questo punto, per tokenizzare una stringa, è sufficiente passarla direttamente all'oggetto tokenizer, ad esempio: token_output = tokenizer('Ecco un esempio pratico di tokenizzazione.'). Il risultato restituito sarà un dizionario contenente diverse chiavi utili per il modello. La chiave 'input_ids' conterrà una lista di interi, dove ogni intero rappresenta l'ID univoco di un token specifico nel vocabolario del modello {model}. La chiave 'attention_mask' conterrà una lista di 1 e 0, utile per indicare al modello quali token sono reali e quali sono stati aggiunti per il padding. A seconda del modello, potresti trovare anche la chiave 'token_type_ids', utilizzata in compiti che richiedono coppie di frasi. Questo meccanismo astrae la complessità della tokenizzazione specifica per ogni modello e fornisce un'interfaccia unificata."

            dataset.append({"instruction": instruction, "output": output})

    with open("dataset_completo.jsonl", "a", encoding="utf-8") as f:
        for item in dataset:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")

if __name__ == "__main__":
    generate_data()
