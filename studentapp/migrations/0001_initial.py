# Generated by Django 3.2.8 on 2021-10-22 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('number', models.IntegerField(unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('image', models.ImageField(default='avatar.png', upload_to='media/students/%Y/%m')),
                ('gender', models.CharField(choices=[('1', 'Female'), ('2', 'Male')], max_length=50)),
            ],
            options={
                'ordering': ('number',),
            },
        ),
    ]
