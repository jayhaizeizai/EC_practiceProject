class EC_Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y =y

    def displayPoint(self):
        print("(",self.x,",",self.y,")")

    def displayPoint_hex(self):
        print("(",hex(self.x),",",hex(self.y),")")

