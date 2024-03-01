from llist import LList, Node, append


def length(lst):
    """return the length of a finite linked list"""
    count = 0
    current = lst.head

    while current is not None:
        count += 1
        current = current .next

        return count


def llprint(lst):
    """print a finite linked list"""
    


if __name__ == "__main__":


#Exersice 1
    llist=LList()
    append(llist, Node(1))
    append(llist, Node(2))
    append(llist, Node(4))
    append(llist, Node(8))
    append(llist, Node(16))
    append(llist, Node(32))
    append(llist, Node(64))
    append(llist, Node(128))
    append(llist, Node(256))
    append(llist, Node(512))
    append(llist, Node(4))

    length(llist)

    print(length(llist))
    
    from genfinite import lst
    print(length(lst))
    pass
    #

    #
