"""Contains main class of the package, TileMap"""


class TileMap:
    def __init__(self, terrains, tiles, metadata) -> None:
        self.terrains = terrains
        self.tiles = tiles
        self.metadata = metadata

    # TODO: implement from_json
    def from_json(self, path: str) -> None:
        pass

    # TODO: implement visualize
    def visualize(self) -> None:
        pass

    # TODO: implement to_json
    def to_json(self, path: str) -> None:
        pass

    # TODO: implement to_image
    def to_image(self, path: str) -> None:
        pass
