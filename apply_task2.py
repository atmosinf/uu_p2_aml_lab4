import json

nb_path = 'AML_assignment4.ipynb'
try:
    with open(nb_path, 'r') as f:
        nb = json.load(f)

    target_str = "def orient_v_structures(self):"
    modified = False
    
    for cell in nb['cells']:
        if cell['cell_type'] == 'code':
            source = cell['source']
            if any(target_str in line for line in source):
                new_source = []
                for line in source:
                    if "# TASK 2: Your code here (2.5 points)" in line:
                        indent_str = line.split('#')[0]
                        new_source.append(line)
                        
                        code_lines = [
                            "        for x in range(self.n):",
                            "            for y in range(x+1, self.n):",
                            "                # Check if x and y are adjacent",
                            "                if self.G[x,y] or self.G[y,x]:",
                            "                    continue",
                            "                # Get separating set",
                            "                S = self.sepset.get(frozenset([x,y]))",
                            "                if S is None:",
                            "                    continue",
                            "",
                            "                # Check all potential shared neighbors z",
                            "                for z in range(self.n):",
                            "                    if z == x or z == y:",
                            "                        continue",
                            "",
                            "                    # Check if z is adjacent to both x and y (undirected or directed)",
                            "                    is_adj_xz = self.G[x,z] or self.G[z,x]",
                            "                    is_adj_yz = self.G[y,z] or self.G[z,y]",
                            "",
                            "                    if is_adj_xz and is_adj_yz:",
                            "                        if z not in S:",
                            "                            # Orient v-structure x -> z <- y",
                            "                            if self.verbose >= 1:",
                            "                                print(f\"Orienting v-structure {self.node_names[x]} -> {self.node_names[z]} <- {self.node_names[y]}\")",
                            "                            self.G[x,z] = True; self.G[z,x] = False",
                            "                            self.G[y,z] = True; self.G[z,y] = False"
                        ]
                        
                        # Apply naive indentation (8 spaces from the method body + 4 spaces for loop? No, the line already has spaces)
                        # The 'line' variable has indentation "        " (8 spaces).
                        # My code_lines assume relatively correct indentation structure, but need to be prepended with base indentation.
                        # Wait, code_lines[0] starts with 8 spaces. That matches "        # TASK 2...".
                        # So I can just append them directly if they are appropriately indented relative to column 0.
                        # My strings in code_lines have appropriate spaces.
                        
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
        print("Successfully modified notebook for Task 2.")
    else:
        print("Could not find the target line to replace.")
        exit(1)

except Exception as e:
    print(f"Error: {e}")
    exit(1)
