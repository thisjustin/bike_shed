from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.management import BaseCommand
from django.contrib.auth.models import User

from apps.bikes.models import Brand, Bike, img_path


class Command(BaseCommand):
    help = 'Save brand(s) to database'

    def handle(self, *args, **options):
        Brand.objects.all().delete()
        Bike.objects.all().delete()
        User.objects.create_superuser(username='root', password='rootpass', email='root@root.root')

        img = SimpleUploadedFile(name='github.jpg', content=open(f'{img_path}github.jpg', 'rb').read(),
                                 content_type='image/jpeg')

        for i in range(5):
            Brand.objects.get_or_create(name=f'Brand #{i + 1}', logo=img)

        for i in range(1, 50):
            user = User.objects.get(id=1)
            brand = Brand.objects.get(id=1)
            Bike.objects.get_or_create(brand=brand, created_by=user, type=f'type #{i}', model=f'model #{i}',
                                       headline=f'headline #{i}', description=f'description #{i}', image=img,
                                       size=i, price=i)
