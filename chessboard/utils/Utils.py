

class Utils:

    def __init__(self):
        pass

    @staticmethod
    def isCollision(pos, allPositions):
        for oPos in allPositions:
            if pos == oPos:
                return True
        return False

