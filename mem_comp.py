# Imports
import pygame


class MemCell:
    """
    Models individual memory cell. Each individual cell is addressed in row, col fashion.
    So row number maps to y and col number maps to x.
    """
    def __init__(self, addr: tuple, cwid=40, chei=40, offset=10):
        self.addr = addr
        self.num_access = 0
        assert isinstance(addr, tuple)
        assert len(addr) == 2
        self.rect = pygame.Rect(offset + addr[1] * cwid, offset + addr[0] * chei, cwid, chei)
        self.color = None
    
    def access(self):
        self.num_access += 1
        self.color = (self.num_access * 10, self.num_access * 10, self.num_access * 10)
    
    def draw(self, screen, font=None):        
        if self.color:
            pygame.draw.rect(screen, self.color, self.rect)
            pygame.draw.rect(screen, (0, 0, 0), self.rect, width=1)
        else:
            pygame.draw.rect(screen, (0, 0, 0), self.rect, 1)
        if font is not None:
            font.render_to(screen, self.rect.topleft, str(self.addr), (0, 0, 0))
            # mdata = font.render(str(self.addr), True, (0, 0, 0))
            # screen.blit(mdata, self.rect.topleft)
            # mdata = font.render(str(self.num_access), True, (0, 0, 0))
            # screen.blit(mdata, self.rect.center)
        

class Mem2D:
    def __init__(self, dimx, dimy):
        self.cells = []
        self.dimx = dimx
        for i in range(dimx):
            for j in range(dimy):
                self.cells.append(MemCell((i, j)))   
    
    def access(self, addr):
        idx = (addr[0] * self.dimx) + addr[1]
        self.cells[idx].access()
    
    def draw(self, screen, font):
        for cell in self.cells:
            cell.draw(screen, font)
        




