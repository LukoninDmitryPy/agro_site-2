# Generated by Django 2.2.16 on 2022-03-21 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_order_status_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status_order',
            field=models.CharField(choices=[('В обработке', 'В обработке'), ('Заказ собран', 'Заказ собран'), ('Заказ отправлен', 'Заказ отправлен')], default='В обработке', max_length=20),
        ),
    ]