from antlr4 import CommonTokenStream, InputStream
from antlr4.error.ErrorListener import ErrorListener
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from antlr4.tree.Tree import TerminalNodeImpl
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import TerminalFormatter


class CustomErrorListener(ErrorListener):
    def __init__(self):
        super(CustomErrorListener, self).__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append(f"line {line}:{column} {msg}")

    def hasErrors(self):
        return len(self.errors) > 0

    def getErrors(self):
        return self.errors


def beautify_tree(tree, parser, indent_level=0):
    if isinstance(tree, TerminalNodeImpl):
        return "    " * indent_level + tree.getText() + "\n"

    rule_name = parser.ruleNames[tree.getRuleIndex()]
    output = "    " * indent_level + rule_name + "\n"

    for child in tree.children:
        output += beautify_tree(child, parser, indent_level + 1)

    return output


# Main script logic
if __name__ == "__main__":
    input_text = input("> ")
    lexer = ExprLexer(InputStream(input_text))
    stream = CommonTokenStream(lexer)
    parser = ExprParser(stream)

    # Add custom error listener
    error_listener = CustomErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)

    tree = parser.program()

    if error_listener.hasErrors():
        print("Errors encountered:")
        for error in error_listener.getErrors():
            print(error)
    else:
        beautified_output = beautify_tree(tree, parser)

        # Optionally, use pygments to highlight the output
        colorful_output = highlight(
            beautified_output, PythonLexer(), TerminalFormatter()
        )

        # Print the beautified (and optionally highlighted) output
        print(colorful_output)
