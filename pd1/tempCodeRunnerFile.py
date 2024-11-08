

def print_tree(node, indent=""):
    if isinstance(node, TerminalNodeImpl):  # Terminal node (e.g., variable, operator, or value)
        # Print the token text for terminal nodes