# Generated by Django 3.2.18 on 2023-03-02 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Hub', '0002_rename_rating_userrating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userrating',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userrating', to='Hub.book'),
        ),
    ]
