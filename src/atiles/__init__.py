"""Contains main class of the package, TileMap"""
import json

from atiles.models import TileMapSchema


# TODO: implement and check functions
# TODO: upload to test pypi
# TODO: implement validation functions
def map_from_json(path: str) -> None:
    with open(path) as f:
        data = json.load(f)
        validated_data = TileMapSchema().load(data=data)
        return TileMap(
            terrains=validated_data["terrains"],
            tiles=validated_data["tiles"],
            metadata=validated_data["metadata"],
        )


class TileMap:
    def __init__(self, terrains, tiles, metadata) -> None:
        self.terrains = terrains
        self.tiles = tiles
        self.metadata = metadata

    # TODO: implement visualize
    def visualize(self) -> None:
        pass

    # TODO: implement to_json
    def to_json(self, path: str) -> None:
        validated_data = TileMapSchema().load(
            data={
                "terrains": self.terrains,
                "tiles": self.tiles,
                "metadata": self.metadata,
            }
        )
        with open(path, "w") as f:
            json.dump(validated_data, f, indent=4, sort_keys=True)

    # TODO: implement to_image
    def to_image(self, path: str) -> None:
        pass
