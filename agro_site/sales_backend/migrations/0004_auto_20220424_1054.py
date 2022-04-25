# Generated by Django 2.2.16 on 2022-04-24 07:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sales_backend', '0003_auto_20220423_1218'),
    ]

    operations = [
        migrations.CreateModel(
            name='RatingStar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.SmallIntegerField(default=0, verbose_name='Значение')),
            ],
            options={
                'verbose_name': 'Звезда рейтинга',
                'verbose_name_plural': 'Звезды рейтинга',
                'ordering': ['-value'],
            },
        ),
        migrations.AlterField(
            model_name='comment',
            name='product',
            field=models.ForeignKey(help_text='Комментарий поста', on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='sales_backend.Product', verbose_name='Комментарий'),
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=15, verbose_name='IP адрес')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales_backend.Product', verbose_name='продукт')),
                ('star', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales_backend.RatingStar', verbose_name='звезда')),
            ],
            options={
                'verbose_name': 'Рейтинг',
                'verbose_name_plural': 'Рейтинги',
            },
        ),
    ]
