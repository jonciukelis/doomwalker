import base
from base import *
import find
from find import *
import move
from move import *


while(1 == 1):
	enemy = findNearestEnemy()
	print json.dumps(enemy, indent=4)
	moveToPoint(enemy["position"]["x"], enemy["position"]["y"])
	

