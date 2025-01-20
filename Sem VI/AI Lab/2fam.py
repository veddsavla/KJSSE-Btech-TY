from graphviz import Digraph
import os

# Add these lines at the start of your code
os.environ["PATH"] += os.pathsep + r'C:\Program Files\Graphviz\bin'
# If you installed to a different location, use that path instead

# Define family relationships
parents = {
    "kantilal": ["mitesh", "milan", "hetal"],
    "saroj": ["mitesh", "milan", "hetal"],
    "premchand": ["priya", "kinal", "rinkal", "payal"],
    "savita": ["priya", "kinal", "rinkal", "payal"],
    "mitesh": ["vedansh"],
    "milan": ["ninjal"],
    "jiten": ["harshay", "mahir"],
    "anup": ["jenil", "ayushi"],
    "shail": ["rian", "shaurya"],
    "vivek": ["praag"],
    "kinal": ["vedansh"],
    "sonal": ["ninjal"],
    "hetal": ["harshay", "mahir"],
    "priya": ["jenil", "ayushi"],
    "rinkal": ["rian", "shaurya"],
    "payal": ["praag"],
}

# Create a directed graph
family_tree = Digraph(format="png")
family_tree.attr(rankdir="TB", size="10")

# Add nodes and edges hierarchically
for parent, children in parents.items():
    for child in children:
        family_tree.node(parent, parent, shape="ellipse", style="filled", fillcolor="skyblue")
        family_tree.node(child, child, shape="ellipse", style="filled", fillcolor="lightgreen")
        family_tree.edge(parent, child)

# Save and render the tree
family_tree.render("family_tree_hierarchical", view=True)
