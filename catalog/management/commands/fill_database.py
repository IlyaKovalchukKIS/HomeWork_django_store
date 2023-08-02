from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        Category.objects.all().delete()

        category_list = [
            {
                "name": "Ноутбук",
                "description": "Многофункциональное устройство для работы и развлечения"
            },
            {
                "name": "Смартфон",
                "description": "Компактное устройсво с огромным функционалом, которое всегда под рукой"
            },
            {
                "name": "Портативная колонка",
                "description": "Устройство для прослушивания ваших любимых треков в хорошем качестве"
            }
        ]

        list_for_category = []
        for category_item in category_list:
            list_for_category.append(Category(**category_item))

        Category.objects.bulk_create(list_for_category)
