# Generated by Django 5.0.2 on 2024-02-23 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0005_alter_group_gadgets'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dream',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('dreams', models.ManyToManyField(related_name='dreams', to='person.person')),
            ],
        ),
    ]
