import base
from base import *
def moveToPoint(destX, destY, attempts=20, pause=1, accuracy=25):
	"""Try to move in a straight line from where we are to a destination
	point in a finite amount of steps. Z axis is disregarded
	"""
	
	for i in range(attempts):
		currentData = getAction('player')
		logging.debug('moveToPoint iteration {} - I am at {} x {} @ {} deg, I need to get to {} x {}'.format(
			i,
			currentData["position"]["x"],
			currentData["position"]["y"],
			currentData["angle"],
			destX,
			destY
		))
		
		distance = distanceBetweenPoints(
			currentData["position"]["x"],
			currentData["position"]["y"],
			destX,
			destY
		)

		#if abs(distance) < 300:
		#	shoot()
		
		if abs(distance) < accuracy:
			logging.debug('moveToPoint is close enough - {} x {} vs {} x {}'.format(
				currentData["position"]["x"],
				currentData["position"]["y"],
				destX,
				destY
			))
			return True
		
		turnToFacePoint(destX, destY)
		
		movePlayer(100)
		
		#time.sleep(pause)
	
	return False
