# Generated by Django 2.2.13 on 2020-07-06 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_cover'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='categorie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='product.Categorie'),
        ),
    ]
