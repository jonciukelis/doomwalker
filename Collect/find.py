import base
from base import *
def findNearestEnemy():
	"""Gets all the world objects, finds the enemies, then
	figures out which one is closest to the player's current
	position. Dumb calculation, does not take map into account.
	"""
	
	playerData = getAction('player')
	worldObjectData = getAction('world/objects')
	
	enemies = []
	
	
	for worldObject in worldObjectData:
		flags = worldObject['flags']
		if u'MF_SPECIAL' in flags:
			print flags
			enemies.append(worldObject)

	logging.debug('Found {} enemies'.format(len(enemies)))
	
	nearestEnemy = None
	nearestEnemyDistance = 999999.0
	
	for enemy in enemies:
			
		distance = distanceBetweenPoints(
			playerData["position"]["x"],
			playerData["position"]["y"],
			enemy["position"]["x"],
			enemy["position"]["y"]
		)
		
		if distance < nearestEnemyDistance:
			logging.debug('Found a new nearest enemy - {}, {} @ {} x {}'.format(
				enemy['id'],
				enemy['type'],
				enemy["position"]["x"],
				enemy["position"]["y"]				
			))
			nearestEnemy = enemy
			nearestEnemyDistance = distance
	
	return nearestEnemy
