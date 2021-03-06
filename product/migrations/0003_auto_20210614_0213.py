# Generated by Django 3.2.4 on 2021-06-14 02:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Allergy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'allergies',
            },
        ),
        migrations.CreateModel(
            name='Nutrition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sodium_mg', models.DecimalField(decimal_places=2, max_digits=6)),
                ('sugars_g', models.DecimalField(decimal_places=2, max_digits=6)),
                ('protein_g', models.DecimalField(decimal_places=2, max_digits=6)),
                ('caffeine_mg', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
            options={
                'db_table': 'nutritions',
            },
        ),
        migrations.CreateModel(
            name='AllergyProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allery', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.allergy')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
            options={
                'db_table': 'allergiesproducts',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='allergy',
            field=models.ManyToManyField(through='product.AllergyProduct', to='product.Allergy'),
        ),
        migrations.AddField(
            model_name='product',
            name='nutrition',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.nutrition'),
        ),
    ]
