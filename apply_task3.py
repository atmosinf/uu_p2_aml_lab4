import json

nb_path = 'AML_assignment4.ipynb'
try:
    with open(nb_path, 'r') as f:
        nb = json.load(f)

    target_str = "def orientation_rules(self):"
    modified = False
    
    for cell in nb['cells']:
        if cell['cell_type'] == 'code':
            source = cell['source']
            if any(target_str in line for line in source):
                new_source = []
                for line in source:
                    if "# TASK 3: Your code here (2.5 points)" in line:
                        
                        code_lines = [
                            "        # Iterate until no more edges can be oriented",
                            "        while True:",
                            "            change = False",
                            "            for x in range(self.n):",
                            "                for y in range(self.n):",
                            "                    # Check Rule 1: x -> y - z => y -> z",
                            "                    # x -> y",
                            "                    if self.G[x,y] and not self.G[y,x]:",
                            "                        for z in range(self.n):",
                            "                            # y - z",
                            "                            if y != z and x != z and self.G[y,z] and self.G[z,y]:",
                            "                                # x and z not adjacent",
                            "                                if not self.G[x,z] and not self.G[z,x]:",
                            "                                    if self.verbose >= 1:",
                            "                                        print(f\"Rule 1: {self.node_names[x]} -> {self.node_names[y]} -> {self.node_names[z]}\")",
                            "                                    self.G[z,y] = False",
                            "                                    change = True",
                            "",
                            "                    # Check Rule 2: x -> y -> z and x - z => x -> z",
                            "                    # x -> y",
                            "                    if self.G[x,y] and not self.G[y,x]:",
                            "                        for z in range(self.n):",
                            "                            # y -> z",
                            "                            if self.G[y,z] and not self.G[z,y]:",
                            "                                # x - z",
                            "                                if self.G[x,z] and self.G[z,x]:",
                            "                                    if self.verbose >= 1:",
                            "                                        print(f\"Rule 2: {self.node_names[x]} -> {self.node_names[z]}\")",
                            "                                    self.G[z,x] = False",
                            "                                    change = True",
                            "",
                            "                    # Check Rule 3: x - y -> z and x - w -> z and y, w non-adjacent => x -> z",
                            "                    # x - z",
                            "                    if self.G[x,y] and self.G[y,x]:",
                            "                         z = y # renaming for clarity matching rule statement: 'x - z' is the potential edge",
                            "                         # Find all nodes 'y' such that x - y -> z",
                            "                         potential_y = []",
                            "                         for v in range(self.n):",
                            "                             if v == x or v == z: continue",
                            "                             # x - v and v -> z",
                            "                             if (self.G[x,v] and self.G[v,x]) and (self.G[v,z] and not self.G[z,v]):",
                            "                                 potential_y.append(v)",
                            "                         ",
                            "                         # Check if any two potential_y nodes are non-adjacent",
                            "                         if len(potential_y) >= 2:",
                            "                             for m, n in itertools.combinations(potential_y, 2):",
                            "                                 if not self.G[m,n] and not self.G[n,m]:",
                            "                                     if self.verbose >= 1:",
                            "                                         print(f\"Rule 3: {self.node_names[x]} -> {self.node_names[z]}\")",
                            "                                     self.G[z,x] = False",
                            "                                     change = True",
                            "                                     break",
                            "            if not change:",
                            "                break"
                        ]
                        
                        for cl in code_lines:
                             new_source.append(cl + "\n")
                        
                        modified = True
                    else:
                        new_source.append(line)
                
                if modified:
                    cell['source'] = new_source
                    break
    
    if modified:
        with open(nb_path, 'w') as f:
            json.dump(nb, f, indent=1)
        print("Successfully modified notebook for Task 3.")
    else:
        print("Could not find the target line to replace.")
        exit(1)

except Exception as e:
    print(f"Error: {e}")
    exit(1)
