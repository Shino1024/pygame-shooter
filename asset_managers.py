class AssetManager:
	__assets = {}

    def load_asset(self, asset_name, asset):
        if asset_name in self.__assets:
					raise ValueError, "The asset with such name has already been loaded."

				self.__assets[asset_name] = asset

class SoundManager(AssetManager):
	#

class SpriteManager(AssetManager):
	pass

class ShapeManager(AssetManager):
	pass

class LevelManager(AssetManager):
	pass
