import pprint

cells={(2,1),(3,2),(1,3),(2,3),(3,3)}
dying={}

def step():
    global cells
    global dying
    neighbors={}
    # TODO need to get rid of nested loops later
    for i in cells:
        x,y=i
        offset=[
            (0,1),
            (1,1),
            (1,0),
            (1,-1),
            (0,-1),
            (-1,-1),
            (-1,0),
            (-1,1),
        ]        
        for nx,ny in offset:
            neighbor=(x+nx,y+ny)
            neighbors[neighbor]=neighbors.get(neighbor,0)+1
    
    # creating the new live cell set

    new_cells=set()

    for i in neighbors:
        if neighbors[i]==3:
            new_cells.add(i)
            continue
        if neighbors[i]==2 and i in cells:
            new_cells.add(i)
            continue
        elif i in cells:
            dying[i]=dying.setdefault(i,3)

    # decrementing dying dict for death animation transitions

    for i in list(dying.keys()):
        if dying[i]==0:
            dying.pop(i)
        else:
            dying[i]=dying[i]-1

    cells=new_cells


# purely for testing purposes
print("Step 1")
step()
pprint.pprint(cells)
pprint.pprint(dying)
print()
print("Step 2")
step()
pprint.pprint(cells)
pprint.pprint(dying)
print()
print("Step 3")
step()
pprint.pprint(cells)
pprint.pprint(dying)
print()
print("Step 4")
step()
pprint.pprint(cells)
pprint.pprint(dying)





