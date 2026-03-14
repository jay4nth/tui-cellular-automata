class Game:
    def __init__(self,cells,dying=None):
        self.cells=cells
        self.dying=dying if dying is not None else {}
        self.offset=[(0,1),
                    (1,1),
                    (1,0),
                    (1,-1),
                    (0,-1),
                    (-1,-1),
                    (-1,0),
                    (-1,1),]  
        
    def step(self):
        neighbors={}
        # TODO need to get rid of nested loops later
        for i in self.cells:
            x,y=i      
            for nx,ny in self.offset:
                neighbor=(x+nx,y+ny)
                neighbors[neighbor]=neighbors.get(neighbor,0)+1
        
        # creating the new live cell set

        new_cells=set()

        for i in neighbors:
            if neighbors[i]==3:
                new_cells.add(i)
                self.dying.pop(i,None)
                continue
            if neighbors[i]==2 and i in self.cells:
                new_cells.add(i)
                self.dying.pop(i,None)
                continue
            elif i in self.cells:
                self.dying[i]=self.dying.setdefault(i,3)

        # decrementing dying dict for death animation transitions

        for i in list(self.dying.keys()):
            if self.dying[i]==0:
                self.dying.pop(i)
            else:
                self.dying[i]=self.dying[i]-1

        self.cells=new_cells





