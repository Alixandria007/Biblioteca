from pathlib import Path

from PIL import Image
from django.conf import settings


def resize_imgs(img,nova_largura = 800 , otimizacao = True , qualidade = 60):
    image_path = Path(settings.MEDIA_ROOT / img.name).resolve()
    image_pillow = Image.open(image_path)
    width, heigth = image_pillow.size

    if width <= nova_largura:
        image_pillow.close()
        return image_pillow
    
    nova_altura = round(nova_largura * heigth / width)

    nova_imagem = image_pillow.resize((nova_largura , nova_altura),Image.LANCZOS)

    nova_imagem.save(
        image_path,
        optimize = otimizacao,
        quality = qualidade
    )

    return nova_imagem