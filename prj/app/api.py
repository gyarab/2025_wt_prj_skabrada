from ninja import NinjaAPI
from models.py import Color

api = NinjaAPI()

@api.get("/color")
def get_color(request):
    color = Colors