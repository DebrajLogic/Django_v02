# Generated by Django 5.0.6 on 2024-06-06 14:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("chai", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="chaivariety",
            name="description",
            field=models.TextField(default=""),
        ),
        migrations.AddField(
            model_name="chaivariety",
            name="price",
            field=models.CharField(default="$4.99", max_length=10),
        ),
    ]
