import json

nb_path = 'AML_assignment4.ipynb'
try:
    with open(nb_path, 'r') as f:
        nb = json.load(f)

    target_str = "# TASK 6: Your code here (1 point)"
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
                        new_source.append("# Alpha of 0.05 is standard, but as the markdown suggests, a larger alpha might be appropriate.\n")
                        new_source.append("# Let's try matching the suggestion or picking a reasonable one like 0.05 first.\n")
                        new_source.append("tester = IndependenceTester(obs_data, alpha=0.05, verbose=1)\n")
                        new_source.append("pc = PC_algorithm(tester, verbose=1)\n")
                        new_source.append("G_obs = pc.run()\n")
                        new_source.append("graph_to_graphviz(G_obs, pc.node_names)\n")
                        modified = True
                    else:
                        new_source.append(line)
                
                if modified:
                    cell['source'] = new_source
                    # We also need to make sure this cell is actually executed to show the output in the notebook if the user runs it.
                    # But we are just editing the source. The user will run it.
                    break
    
    if modified:
        with open(nb_path, 'w') as f:
            json.dump(nb, f, indent=1)
        print("Successfully modified notebook for Task 6.")
    else:
        print("Could not find the target line to replace.")
        exit(1)

except Exception as e:
    print(f"Error: {e}")
    exit(1)
