from typing import List
from django.shortcuts import get_object_or_404
from .models import Color
from .schemas import ColorSchema, ColorCreateSchema
from ninja import NinjaAPI

api = NinjaAPI()


@api.get("/color", response=List[ColorSchema])
def list_colors(request):
    return Color.objects.all()


@api.get("/color/{color_id}", response=ColorSchema)
def get_color(request, color_id: int):
    return get_object_or_404(Color, id=color_id)


@api.post("/color", response=ColorSchema)
def create_color(request, data: ColorCreateSchema):
    return Color.objects.create(**data.dict())


@api.put("/color/{color_id}", response=ColorSchema)
def update_color(request, color_id: int, data: ColorCreateSchema):
    color = get_object_or_404(Color, id=color_id)
    color.name = data.name
    color.hex_id = data.hex_id
    color.save()
    return color