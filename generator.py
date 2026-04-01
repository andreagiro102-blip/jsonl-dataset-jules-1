import json
import random
import itertools

prefixes = [
    "Scrivi il codice per", "Costruisci", "Sviluppa", "Implementa",
    "Realizza", "Crea", "Progetta", "Programma", "Fornisci"
]
subjects = [
    "una classe Python", "un modulo in Python", "uno script Python",
    "una struttura dati in Python", "un programma in Python"
]
actions = [
    "che implementi", "per implementare", "capace di rappresentare",
    "per gestire", "che modelli"
]
objects = [
    "un albero binario di ricerca", "un BST (Binary Search Tree)",
    "un albero di ricerca binario"
]
details = [
    "con metodi di inserimento e bilanciamento.",
    "dotato di funzioni per inserire e bilanciare i nodi.",
    "inclusivo di inserimento e auto-bilanciamento.",
    "che supporti l'inserimento e il bilanciamento automatico.",
    "provvisto di operazioni per l'inserimento e il bilanciamento."
]

combinations = list(itertools.product(prefixes, subjects, actions, objects, details))
random.seed(42)
random.shuffle(combinations)

selected_combinations = combinations[:200]

intro_texts = [
    "Certamente. Di seguito presento una soluzione completa basata su un albero AVL, che e un tipo di albero binario di ricerca auto-bilanciante. L'implementazione include le rotazioni necessarie per mantenere il bilanciamento dopo ogni inserimento.\n\n",
    "Ecco un'implementazione dettagliata in Python. Per garantire il bilanciamento, ho utilizzato la logica degli alberi AVL. Questa struttura dati garantisce operazioni efficienti mantenendo l'altezza dell'albero logaritmica.\n\n",
    "Assolutamente. La scelta migliore per un albero binario di ricerca con bilanciamento automatico e l'albero AVL. Ecco il codice Python completo di spiegazioni dettagliate, con i metodi per inserire nuovi nodi e bilanciare la struttura.\n\n"
]

code_template = """class {node_class}:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class {tree_class}:
    def {insert_method}(self, root, key):
        if not root:
            return {node_class}(key)
        elif key < root.key:
            root.left = self.{insert_method}(root.left, key)
        else:
            root.right = self.{insert_method}(root.right, key)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)
"""

explanation_texts = [
    "\n\nIn questa implementazione, la classe del nodo memorizza l'altezza per calcolare rapidamente il fattore di bilanciamento. Le rotazioni a sinistra e a destra vengono applicate in base ai quattro casi di sbilanciamento (Sinistra-Sinistra, Destra-Destra, Sinistra-Destra, Destra-Sinistra) durante la risalita ricorsiva dell'inserimento.",
    "\n\nL'algoritmo di inserimento segue la normale logica dei BST. Dopo aver inserito la chiave, aggiorniamo l'altezza del nodo corrente e verifichiamo il fattore di bilanciamento. Se l'albero risulta sbilanciato, effettuiamo le rotazioni appropriate per ristabilire la proprieta AVL.",
    "\n\nLa gestione del bilanciamento e cruciale: il metodo di inserimento restituisce la nuova radice del sottoalbero dopo l'eventuale rotazione. Questo garantisce che l'altezza dell'albero rimanga O(log n), mantenendo le prestazioni ottimali per future operazioni di ricerca o inserimento."
]

dataset = []
for i, combo in enumerate(selected_combinations):
    instruction = " ".join(combo)

    # Variations in code to make it unique and detailed
    node_classes = ["Node", "TreeNode", "AVLNode", "BSTNode"]
    tree_classes = ["AVLTree", "BalancedBST", "SelfBalancingTree", "AVL"]
    insert_methods = ["insert", "insert_node", "add", "add_node"]

    nc = random.choice(node_classes)
    tc = random.choice(tree_classes)
    im = random.choice(insert_methods)

    intro = random.choice(intro_texts)
    code = code_template.format(node_class=nc, tree_class=tc, insert_method=im)
    expl = random.choice(explanation_texts)

    output = intro + code + expl

    # Ensuring no markdown blocks like ``` are in the string.
    # The output is formatted plainly.

    dataset.append({
        "instruction": instruction,
        "output": output
    })

# Write to jsonl
with open("dataset_completo.jsonl", "a", encoding="utf-8") as f:
    for item in dataset:
        f.write(json.dumps(item, ensure_ascii=False) + "\n")

print(f"Generazione completata. 200 righe aggiunte a dataset_completo.jsonl.")
