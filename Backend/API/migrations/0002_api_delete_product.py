# Generated by Django 4.0.5 on 2022-08-27 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='API',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('location', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]