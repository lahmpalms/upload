# Generated by Django 3.2.5 on 2021-09-21 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uploadimg', '0009_frame'),
    ]

    operations = [
        migrations.AddField(
            model_name='care',
            name='frame',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='uploadimg.frame'),
        ),
    ]