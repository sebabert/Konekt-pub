# Generated by Django 3.1.6 on 2021-05-26 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('konekt', '0008_auto_20210503_1034'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='scrapping_id',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
