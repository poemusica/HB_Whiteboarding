#!/usr/bin/env python

class BinaryTreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def tokenize(string):
    return string.replace("(", " ( ").replace(")", " ) ").split()

def consume(token_list):
    return token_list.pop(0)

def has_precedence(o1, o2):
    # if o1 is weaker than or equal to that of o2, return False
    if o2.value == '*' or o2.value == '/':
        return False
    if (o2.value == '+' or o2.value == '-') and (o1 == '+' or o1 == '-'):
        return False
    # if o1 is stronger than o2, return True
    return True

def build_parse_tree(token_list):
    # IMPLEMENT SHUNTING YARD ALGORITHM HERE
    output_queue = [] # has nodes. NOTE: This is actually a stack!!
    stack = [] # has nodes

#   While there are tokens to be read:
    while token_list:
        # Read a token.
        token = consume(token_list)

        # If the token is a number, then add it to the output queue.
        if is_num(token):
            output_queue.append(BinaryTreeNode(int(token)))
        
        # If the token is an operator, o1
        if token in ['+', '-', '/', '*']:
            # while there is an operator token, o2, at the top of the stack, and
            #   - either o1 is left-associative and its precedence is less than or equal to that of o2,
            #   - or o1 has precedence less than that of o2,
            while (stack[-1].value in ['+', '-', '/', '*']) and (not has_precedence(token, stack[-1])):
                # pop o2 off the stack
                op_2 = stack.pop()
                # combine it with the last two elements on the queue to produce a binary tree node
                node = BinaryTreeNode(op_2.value)
                node.right = output_queue.pop(-1)
                node.left = output_queue.pop(-1)
                # then push that node onto the output queue.
                output_queue.append(node)
            # push o1 onto the stack
            stack.append(BinaryTreeNode(token))
        
        # If the token is a left parenthesis, then push it onto the stack.
        if token == '(':
            stack.append(BinaryTreeNode(token))
        
        # If the token is a right parenthesis:
        if token == ')':
            # Until the token at the top of the stack is a left parenthesis,
            while stack[-1].value != '(':
                # pop operators off the stack
                op = stack.pop()
                 # combine them with the last two elements on the queue to create a binary tree node 
                node = BinaryTreeNode(op.value)
                # node.left = output_queue.pop(0)
                # node.right = output_queue.pop(0)
                node.right = output_queue.pop(-1)
                node.left = output_queue.pop(-1)
                # put that node on the stack.
                output_queue.append(node)
            if stack[-1].value == '(':
                # Pop the left parenthesis from the stack, but not onto the output queue.
                stack.pop()
            # If the stack runs out without finding a left parenthesis, 
            # then there are mismatched parentheses
            else:
                print 'Error: mismatched parentheses 1.'
                return


        # While there are still operator tokens in the stack:
    for n in stack:
        print n.value
    while stack:
        # If the operator token on the top of the stack is a parenthesis, 
        # then there are mismatched parentheses.
        if stack[-1].value in ['(', ')']:
            print 'Error: mismatched parentheses 2.'
            return
        if stack[-1].value in ['+', '-', '/', '*']:
            # Pop the operator off the stack
            op = stack.pop()
             # combine it with the last two elements on the queue to produce a binary tree node
            node = BinaryTreeNode(op.value)
            node.left = output_queue.pop(-1)
            node.right = output_queue.pop(-1)
            # then push that node onto the output queue.
            print "appending %r" % node.value
            output_queue.append(node)

    # Return the final node on the output queue
    return output_queue[0]

def is_num(string):
    try:
        int(string)
        return True
    except:
        return False

def evaluate_tree(node):
    if node is None:
        return
    if type(node.value) == int:
        return node.value
    elif node.value == "+":
        return evaluate_tree(node.left) + evaluate_tree(node.right)
    elif node.value == "*":
        return evaluate_tree(node.left) * evaluate_tree(node.right)
    elif node.value == "/":
        return evaluate_tree(node.left) / evaluate_tree(node.right)
    elif node.value == "-":
        return evaluate_tree(node.left) - evaluate_tree(node.right)

def main():
    sample_string = "(((3 + 2) * (4 - 1) / 3 + 7) * (1 + (-5 + 6)))"
    print "answer should be: %d" % (((3 + 2) * (4 - 1) / 3 + 7) * (1 + (-5 + 6)))
    tokens = tokenize(sample_string)
    tree = build_parse_tree(tokens)
    print evaluate_tree(tree)

if __name__ == "__main__":
    main()
