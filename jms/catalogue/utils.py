import uuid
from django.utils.text import slugify


def product_image_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    store_name = slugify(instance.store.name)
    return f'images/store/{store_name}/products/{filename}'