class TreeNode :
    leftNode = None
    rightNode = None
    value: int = None
    level: int = None
    def __init__(self, value: int):
        """
        :type value: int
        """
        self.value = value