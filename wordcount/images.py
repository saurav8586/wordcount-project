from PIL import Image
from django.http import HttpResponse

try:
    img = Image.open("C:/Users/sp858/Downloads/basara.png")
except IOError:
    print('Cant Open')
def image(request):
    return HttpResponse("C:/Users/sp858/Downloads/basara.png")
