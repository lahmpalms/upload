# Generated by Django 3.2.5 on 2021-08-10 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploadimg', '0003_alter_care_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='care',
            name='detail',
            field=models.TextField(),
        ),
    ]