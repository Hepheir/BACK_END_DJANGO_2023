# Generated by Django 4.2.1 on 2023-05-10 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("post", "0002_post_title"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="created_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
