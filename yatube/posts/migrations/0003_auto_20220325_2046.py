# Generated by Django 2.2.19 on 2022-03-25 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20220325_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='group',
            field=models.ForeignKey(blank=True, max_length=200, null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.Group'),
        ),
    ]
