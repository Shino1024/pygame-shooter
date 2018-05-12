class MapElement:
	def __init__(self, obj):
		self.info = (key: value for key: value in obj.iteritems() if key not in ["x", "y", "field_type"]}
		self.x = obj.x
		self.y = obj.y
		self.field_type = obj.field_type

class Map:
	map_grid = [[]]
