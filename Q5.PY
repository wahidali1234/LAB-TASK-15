class ExpressionTreeNode:
    def _init_(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def construct_expression_tree(postfix):
    stack = []
    for token in postfix:
        if token.isdigit():
            stack.append(ExpressionTreeNode(int(token)))
        else:
            right = stack.pop()
            left = stack.pop()
            stack.append(ExpressionTreeNode(token, left, right))
    return stack.pop()