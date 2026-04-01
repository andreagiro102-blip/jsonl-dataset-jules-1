import json

with open("dataset_completo.jsonl", "r", encoding="utf-8") as f:
    for i, line in enumerate(f):
        try:
            data = json.loads(line)
            assert "instruction" in data
            assert "output" in data
        except Exception as e:
            print(f"Error on line {i+1}: {e}")
            break
    else:
        print("All lines are valid JSON objects with 'instruction' and 'output' keys.")
