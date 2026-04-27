from ninja import Schema

class ColorSchema(Schema):
    id: int
    name: str
    hex_id: str


class ColorCreateSchema(Schema):
    name: str
    hex_id: str