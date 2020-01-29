def chickdog(head, leg):
    chick = int(0.5*(4*head - leg))
    dog = int(head - chick)
    if ( chick >= 0
        and dog >= 0
        and (chick + dog == head)
        and (2*chick + 4*dog == leg) ):
        return [chick, dog]
    else:
        return None
