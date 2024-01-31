from flask_frozen import Freezer
from app import HS
freezer = Freezer(HS)
if __name__ == '__main__':
    freezer.freeze()