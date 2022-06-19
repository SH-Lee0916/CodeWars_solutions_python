'''
https://www.codewars.com/kata/52a89c2ea8ddc5547a000863
'''
def loop_size(node):
    node_list = [node]
    
    while node.next not in node_list:
        node = node.next
        node_list.append(node)
        
    
    start_node_idx = node_list.index(node.next)
    
    return len(node_list[start_node_idx:])


if __name__ == "__main__":
    class Node():
        def __init__(self):
            self.next = None
            
    # Make a short chain with a loop of 3
    node1 = Node()
    node2 = Node()
    node3 = Node()
    node4 = Node()
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2
    print(loop_size(node1), 3, 'Loop size of 3 expected')