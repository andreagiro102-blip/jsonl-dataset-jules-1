import json
import random

prefixes = [
    "Ciao, ",
    "Per favore, ",
    "Potresti ",
    "Ho bisogno di ",
    "Mi servirebbe ",
    "Saresti in grado di ",
    "Vorrei ",
    "Fammi vedere come ",
    "Aiutami a ",
    ""
]

cores = [
    "scrivere un Dockerfile ottimizzato per un'applicazione basata su FastAPI e PyTorch",
    "creare un Dockerfile efficiente per un'app FastAPI con PyTorch",
    "costruire un Dockerfile per FastAPI e PyTorch che sia leggero e performante",
    "realizzare un'immagine Docker ottimizzata per PyTorch e FastAPI",
    "preparare un Dockerfile di produzione per un'API FastAPI che usa PyTorch",
    "strutturare un Dockerfile per un progetto FastAPI e PyTorch",
    "configurare un Dockerfile per fare il deploy di FastAPI con PyTorch",
    "sviluppare un Dockerfile ottimizzato (FastAPI + PyTorch)",
    "fare un Dockerfile per inferenza con PyTorch esposta via FastAPI",
    "mettere in un container Docker un'app FastAPI e PyTorch in modo ottimale"
]

suffixes = [
    ". Grazie.",
    ". Te ne sarei grato.",
    ". È per un progetto in produzione.",
    ". Mi serve per il deploy.",
    ". Voglio mantenere l'immagine il più piccola possibile.",
    ". Considera l'uso di multistage build se utile.",
    ". Spiegami anche le scelte che hai fatto.",
    ". Assicurati che le dipendenze siano installate correttamente.",
    ". Il container deve essere pronto per l'ambiente cloud.",
    "."
]

base_images = [
    "python:3.9-slim",
    "python:3.10-slim",
    "python:3.11-slim",
    "python:3.9-slim-buster",
    "python:3.10-slim-bullseye",
    "nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu22.04"
]

def generate_output(idx, base_image):
    is_gpu = "nvidia" in base_image

    explanation_intro = [
        "Certamente! Ecco un Dockerfile ottimizzato per la tua applicazione FastAPI e PyTorch.",
        "Assolutamente. Di seguito trovi una proposta di Dockerfile per FastAPI e PyTorch, pensata per la produzione.",
        "Ecco un esempio di Dockerfile efficiente per il tuo stack FastAPI + PyTorch.",
        "Certo, ti mostro come strutturare il Dockerfile per ottenere un'immagine leggera e sicura con FastAPI e PyTorch."
    ]

    explanation_mid = [
        "Ho utilizzato una build ottimizzata per ridurre le dimensioni del livello finale. ",
        "Il codice sfrutta le best practice come la copia separata di requirements.txt per usare la cache di Docker. ",
        "Ho impostato un utente non-root per ragioni di sicurezza. ",
        "Viene installata solo la versione CPU di PyTorch per risparmiare spazio, a meno che non sia esplicitamente richiesto il supporto GPU. "
    ]
    if is_gpu:
        explanation_mid.append("In questo caso ho scelto un'immagine di base NVIDIA per avere il supporto CUDA out-of-the-box. ")

    explanation_outro = [
        "Puoi eseguire questo container mappando la porta 8000.",
        "Ricordati di costruire l'immagine con 'docker build -t fastapi-pytorch .'.",
        "Questo approccio garantisce un tempo di avvio rapido e un ingombro di memoria ridotto.",
        "Assicurati di avere gunicorn e uvicorn nel tuo requirements.txt."
    ]

    dockerfile_cpu = f"""
FROM {base_image} as builder
WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends build-essential \\
    && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

FROM {base_image}
WORKDIR /app
COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH
COPY . .
RUN useradd -m appuser && chown -R appuser /app
USER appuser
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
"""

    dockerfile_gpu = f"""
FROM {base_image}
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends python3 python3-pip \\
    && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt --extra-index-url https://download.pytorch.org/whl/cu118
COPY . .
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
"""

    df = dockerfile_gpu if is_gpu else dockerfile_cpu

    output_text = (
        random.choice(explanation_intro) + " " +
        random.choice(explanation_mid) + "\n\n" +
        "DOCKERFILE:\n" +
        df.strip() + "\n\n" +
        "SPIEGAZIONE:\n" +
        "- Usa " + base_image + " come base.\n" +
        "- Installa le dipendenze in modo efficiente sfruttando il layer caching.\n" +
        "- " + random.choice(explanation_outro)
    )
    return output_text

generated_pairs = set()
dataset = []

while len(dataset) < 200:
    p = random.choice(prefixes)
    c = random.choice(cores)
    s = random.choice(suffixes)

    instruction = f"{p}{c}{s}"

    if instruction not in generated_pairs:
        generated_pairs.add(instruction)
        base_img = random.choice(base_images)
        output_text = generate_output(len(dataset), base_img)

        dataset.append({
            "instruction": instruction.strip(),
            "output": output_text
        })

# append to the file
with open('dataset_completo.jsonl', 'a', encoding='utf-8') as f:
    for item in dataset:
        f.write(json.dumps(item, ensure_ascii=False) + '\n')

print(f"Generazione completata: {len(dataset)} righe aggiunte.")
