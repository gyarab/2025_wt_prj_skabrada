from ninja import Schema


class ColorSchema(Schema):
    id: int
    name: str
    hex_id: str
    info_misc: str | None = None


class ColorCreateSchema(Schema):
    name: str
    hex_id: str
    info_misc: str | None = None