from csv import DictReader
from xml.dom.xmlbuilder import _DOMInputSourceStringDataType

from django.core.management import BaseCommand
from sales_backend.models import Product

CATALOG = {
    Product : 'products.csv'
}

class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        print('\tstart Scanning')

        for model, data in CATALOG.items():

            print(f'Loading {data} data')
            
            for row in DictReader(
                open(f'static/data/{data}', 'r', encoding='utf-8'),
                delimiter=';'
            ):
                created = model(
                    id=row['id'],
                    name=row['name'],
                    product_group_id=row['folder'],
                    product_seller_id=row['supplier'],
                    image=row['image'],
                    price=row['price'],
                    description=row['description'],
                    count=row['amount'],
                    discount=row['discount'],
                    on_sale=row['onsale'],   
                )
                created.save()
        self.stdout.write(self.style.SUCCESS(' Ready '))