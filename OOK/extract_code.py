import json

notebook_path = r'z:\Documents\GitHub\Communications_Engineering\OOK\OOK_modulation.ipynb'

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'code':
        print(f"--- Cell {i} ---")
        print(''.join(cell['source']))
        print("\n")
