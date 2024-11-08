import sys
from antlr4 import *
from python_pd1Lexer import python_pd1Lexer
from python_pd1Parser import python_pd1Parser
from antlr4.tree.Tree import TerminalNodeImpl


#I just took this function from this guys github so I could debug the parse tree in a neater format.
#https://github.com/parrt


def print_tree(node, indent=""):
    if isinstance(node, TerminalNodeImpl): 
    
        print(f"{indent}{node.getText()}")
    else:
        rule_name = python_pd1Parser.ruleNames[node.getRuleIndex()]
        
        if rule_name == "program":
            print("Program")
            print(f"{indent}└── Statements")
            for child in node.getChildren():
                print_tree(child, indent + "    ")
        elif rule_name == "statement":
           
            print(f"{indent}├── Assignment")
            for child in node.getChildren():
                print_tree(child, indent + "│   ")
        elif rule_name == "assignment":
            
            variable = node.getChild(0).getText()
            operator = node.getChild(1).getText()
            print(f"{indent}├── Variable: {variable}")
            print(f"{indent}├── Operator: {operator}")
            print(f"{indent}└── Value:")
            print_tree(node.getChild(2), indent + "    ")
        elif rule_name == "expression":
            if node.getChildCount() == 1:
                print(f"{indent}{node.getChild(0).getText()}")
            else:
                for child in node.getChildren():
                    print_tree(child, indent + "    ")
        else:
            for child in node.getChildren():
                print_tree(child, indent + "    ")



def main():
    with open("parser/pd1/project_deliverable_1.py", "r") as file:
        input_code = file.read()

    input_stream = InputStream(input_code)
    lexer = python_pd1Lexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = python_pd1Parser(token_stream)
    tree = parser.program()
    print(tree.toStringTree(recog=parser))

    for _ in range(5):
        print() 

    print_tree(tree) 

if __name__ == "__main__":
    main()




