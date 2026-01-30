import json
import itertools

nb_path = 'AML_assignment4.ipynb'
try:
    with open(nb_path, 'r') as f:
        nb = json.load(f)

    # Find the cell
    target_str = "class PC_algorithm:"
    modified = False
    
    for cell in nb['cells']:
        if cell['cell_type'] == 'code':
            source = cell['source']
            # source is a list of strings. Join them to search, or search line by line.
            # We need to preserve the list structure.
            
            # Check if this is the right cell
            if any(target_str in line for line in source):
                new_source = []
                for line in source:
                    if "for S in []: # replace this line by your code" in line:
                        # Calculate indentation (count spaces at start)
                        indent_str = ""
                        for char in line:
                            if char == ' ':
                                indent_str += " "
                            else:
                                break
                        
                        # Add new lines with correct indentation
                        new_source.append(indent_str + "# TASK 1 implementation\n")
                        new_source.append(indent_str + "# Get neighbors of x, excluding y\n")
                        new_source.append(indent_str + "neighbors = [n for n in range(self.n) if self.G[x, n] and n != y]\n")
                        new_source.append(indent_str + "# Iterate over all subsets S of size k of these neighbors\n")
                        new_source.append(indent_str + "for S in itertools.combinations(neighbors, k):\n")
                        new_source.append(indent_str + "    S = list(S)\n")
                        modified = True
                    else:
                        new_source.append(line)
                
                if modified:
                    cell['source'] = new_source
                    break
    
    if modified:
        with open(nb_path, 'w') as f:
            json.dump(nb, f, indent=1)
        print("Successfully modified notebook.")
    else:
        print("Could not find the target line to replace.")
        exit(1)

except Exception as e:
    print(f"Error: {e}")
    exit(1)
