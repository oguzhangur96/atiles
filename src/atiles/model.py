"""General JSON schema of map configuration. Advanced validation will be written in map class."""

from marshmallow import Schema, fields, validate


class TileMapMetadata(Schema):
    name = fields.String(required=True)
    max_x = fields.Int(validate.Range(min=0, min_inclusive=True), required=True)
    max_y = fields.Int(validate.Range(min=0, min_inclusive=True), required=True)
    description = fields.String(required=False)


class RGBCode(Schema):
    R = fields.Integer(
        validate=validate.Range(min=0, min_inclusive=True, max=255, max_inclusive=True)
    )
    G = fields.Integer(
        validate=validate.Range(min=0, min_inclusive=True, max=255, max_inclusive=True)
    )
    B = fields.Integer(
        validate=validate.Range(min=0, min_inclusive=True, max=255, max_inclusive=True)
    )


class Terrain(Schema):
    name = fields.String(required=True)
    description = fields.String(required=False)
    color_code = fields.Nested(RGBCode(), required=True)


class Tile(Schema):
    x = fields.Int(required=True)
    y = fields.Int(required=True)
    terrain = fields.Nested(Terrain, required=True)


class TileMapMetadata(Schema):
    metadata = fields.Nested(TileMapMetadata(), required=True)
    terrains = fields.Nested(Terrain(), required=True)
    tiles = fields.List(fields.Nested(Tile), required=True)
