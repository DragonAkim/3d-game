class Block():
    def __init__(self):
        self.data = []
        self.__namenum = 1
    def add_block(self, x0, y0, x1, y1, blocktype, blockname="Default"):
        if x0 > x1:
            replacor = x0
            x0 = x1
            x1 = replacor
        if y0 > y1:
            replacor = y0
            y0 = y1
            y1 = replacor
        if blockname == "Default":
            blockname = f"{self.__namenum}"
            self._Block__namenum += 1
        self.data.append([[[x0, y0], [x1, y1]], blocktype, blockname])
    def delete_block(self, blockname):
        for i in range(len(self.data)): 
            if self.data[i][2] == blockname: break
        self.data.pop(i)
    