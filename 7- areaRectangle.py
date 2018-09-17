def areaRectangle(ln, br=1):
    '''
    OBJECTIVE:   To find the area of a rectangle of given length and breadth.
    INPUT:
        ln:   A positive integer depicting the length of the given rectangle.
        br:   A positive integer depicting the breadth of the given rectangle.
    OUTPUT:
        The area of the given rectangle.
    '''
    #APPROACH: areaRectangle(ln, br) = ln * br

    assert ln > 0
    assert br > 0
    
    area = ln * br

    return area
