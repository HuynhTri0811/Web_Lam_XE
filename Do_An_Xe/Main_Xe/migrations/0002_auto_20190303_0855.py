# Generated by Django 2.1.5 on 2019-03-03 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main_Xe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hangsanxuat',
            name='HinhURL_HSX',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
