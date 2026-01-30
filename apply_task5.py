import json

nb_path = 'AML_assignment4.ipynb'
try:
    with open(nb_path, 'r') as f:
        nb = json.load(f)

    target_str = "# TASK 5: Your code here (0.5 point)"
    modified = False
    
    for cell in nb['cells']:
        if cell['cell_type'] == 'code':
            source = cell['source']
            if any(target_str in line for line in source):
                new_source = []
                for line in source:
                    if target_str in line:
                        new_source.append(line)
                        new_source.append("\n")
                        new_source.append("obs_data = all_data[all_data['experiment'] == 1].copy()\n")
                        new_source.append("obs_data = obs_data.drop(columns=['experiment'])\n")
                        new_source.append("print(f'Shape of obs_data: {obs_data.shape}')\n")
                        modified = True
                    else:
                        new_source.append(line)
                
                if modified:
                    cell['source'] = new_source
                    break
    
    if modified:
        with open(nb_path, 'w') as f:
            json.dump(nb, f, indent=1)
        print("Successfully modified notebook for Task 5.")
    else:
        print("Could not find the target line to replace.")
        exit(1)

except Exception as e:
    print(f"Error: {e}")
    exit(1)
