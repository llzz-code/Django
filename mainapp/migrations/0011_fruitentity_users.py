# Generated by Django 2.0.1 on 2021-04-10 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_realprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='fruitentity',
            name='users',
            field=models.ManyToManyField(db_table='t_collect', related_name='fruits', to='mainapp.UserEntity', verbose_name='收藏用户列表'),
        ),
    ]
