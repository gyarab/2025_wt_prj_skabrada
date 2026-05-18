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


@api.put("/color/{color_id}/", response=ColorSchema)
def update_color(request, color_id: int, data: ColorCreateSchema):

    color = get_object_or_404(Color, id=color_id)

    color.name = data.name
    color.hex_id = data.hex_id
    color.info_misc = data.info_misc

    color.save()

    return color


@api.put("/color/{color_id}", response=ColorSchema)
def update_color(request, color_id: int, data: ColorCreateSchema):
    color = get_object_or_404(Color, id=color_id)
    color.name = data.name
    color.hex_id = data.hex_id
    color.save()
    return color

@api.delete("/color/{color_id}/")
def delete_color(request, color_id: int):
    color = get_object_or_404(Color, id=color_id)
    color.delete()

    return {"success": True}