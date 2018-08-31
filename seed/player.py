from seed import Seed


class Player(Seed):

	def __init__(self, x=0, y=0):
		"""
		initialize unique attributes of Player
		"""
		super().__init__(x,y)

	def update(self):
		"""
		overrided to include unique attributes of Player
		"""
		pass
