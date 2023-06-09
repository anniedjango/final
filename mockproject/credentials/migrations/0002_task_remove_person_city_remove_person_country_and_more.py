# Generated by Django 4.1.3 on 2023-04-28 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credentials', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('lastname', models.CharField(max_length=250, null=True)),
                ('date', models.DateField()),
                ('email', models.EmailField(max_length=254, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='person',
            name='city',
        ),
        migrations.RemoveField(
            model_name='person',
            name='country',
        ),
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='Country',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
