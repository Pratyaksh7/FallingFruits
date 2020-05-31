# Generated by Django 3.0.5 on 2020-05-29 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0002_auto_20200524_2117'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(upload_to='shop/images')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.Location')),
            ],
        ),
    ]