import json

nb_path = 'AML_assignment4.ipynb'
try:
    with open(nb_path, 'r') as f:
        nb = json.load(f)

    # Question 9: Scatterplot for PIP2 and PIP3 (or neighbor)
    target_str_9 = "**Question 9 (2 points)**"
    # We want to add code AFTER this markdown cell. 
    # Usually there is an empty code cell or "Task XX: Your code here" after question. 
    # But Q9 asks to "Insert one or more markdown and code boxes below here".
    # I'll look for the cell containing the question text and insert a code cell after it.
    
    modified = False
    new_cells = []
    
    for cell in nb['cells']:
        new_cells.append(cell)
        
        # Check for Question 9
        if cell['cell_type'] == 'markdown' and target_str_9 in ''.join(cell['source']):
            # Add plotting code for Q9
            code_source_9 = [
                "# Visualization for Question 9\n",
                "import matplotlib.pyplot as plt\n",
                "import seaborn as sns\n",
                "\n",
                "# Assuming PIP3 is the neighbor of PIP2 based on typical results. \n",
                "# If the user's graph is different, they might need to change 'PIP3' to the actual neighbor.\n",
                "neighbor = 'PIP3' \n",
                "\n",
                "plt.figure(figsize=(10, 5))\n",
                "sns.scatterplot(data=data_1_5, x='PIP2', y=neighbor, hue='experiment', palette='viridis', alpha=0.6)\n",
                "plt.title(f'Scatterplot of PIP2 vs {neighbor} (Exp 1 & 5)')\n",
                "plt.show()\n"
            ]
            
            new_code_cell_9 = {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": code_source_9
            }
            new_cells.append(new_code_cell_9)
            modified = True
            
        # Check for Question 10
        if cell['cell_type'] == 'markdown' and "**Question 10 (2 points)**" in ''.join(cell['source']):
             # Add plotting code for Q10
            code_source_10 = [
                "# Visualization for Question 10\n",
                "# pmek and perk interact. We look at them in Exp 1 and 6.\n",
                "plt.figure(figsize=(10, 5))\n",
                "sns.scatterplot(data=data_1_6, x='pmek', y='perk', hue='experiment', palette='viridis', alpha=0.6)\n",
                "plt.title('Scatterplot of pmek vs perk (Exp 1 & 6)')\n",
                "plt.show()\n"
            ]
            
            new_code_cell_10 = {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": code_source_10
            }
            new_cells.append(new_code_cell_10)
            modified = True

    if modified:
        nb['cells'] = new_cells
        with open(nb_path, 'w') as f:
            json.dump(nb, f, indent=1)
        print("Successfully added plotting code for Q9 and Q10.")
    else:
        print("Could not find the target cells.")

except Exception as e:
    print(f"Error: {e}")
    exit(1)
