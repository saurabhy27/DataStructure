class BNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self) -> str:
        return "Data {} left {} right {}".format(self.data, self.left, self.right)
