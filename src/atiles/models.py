"""General JSON schema of map configuration. Advanced validation will be written in map class."""

from marshmallow import Schema, fields, validate


class TileMapMetadata(Schema):
    name = fields.String(required=True)
    max_x = fields.Int(
        validate=validate.Range(min=0, min_inclusive=True), required=True
    )
    max_y = fields.Int(
        validate=validate.Range(min=0, min_inclusive=True), required=True
    )
    description = fields.String(required=False)


class RGBCode(Schema):
    R = fields.Integer(
        validate=validate.Range(min=0, min_inclusive=True, max=255, max_inclusive=True),
        required=True,
    )
    G = fields.Integer(
        validate=validate.Range(min=0, min_inclusive=True, max=255, max_inclusive=True),
        required=True,
    )
    B = fields.Integer(
        validate=validate.Range(min=0, min_inclusive=True, max=255, max_inclusive=True),
        required=True,
    )


class Terrain(Schema):
    name = fields.String(required=True)
    description = fields.String(required=False)
    color_code = fields.Nested(RGBCode(), required=True)


class Tile(Schema):
    x = fields.Int(
        validate=validate.Range(
            min=0, min_inclusive=False, max=255, max_inclusive=True
        ),
        required=True,
    )
    y = fields.Int(
        validate=validate.Range(
            min=0, min_inclusive=False, max=255, max_inclusive=True
        ),
        required=True,
    )
    terrain_name = fields.Str(required=True)


class TileMapSchema(Schema):
    metadata = fields.Nested(TileMapMetadata(), required=True)
    terrains = fields.List(fields.Nested(Terrain()), required=True)
    tiles = fields.List(fields.Nested(Tile()), required=True)
