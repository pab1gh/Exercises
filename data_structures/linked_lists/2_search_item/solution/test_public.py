def test_solution():
    from solution import Node, linkedList

    items = linkedList()
    items.head = Node(20)
    items.head.next = Node(30)
    items.head.next.next = Node(40)

    assert items.search(30) == True
    assert items.search(10) == False