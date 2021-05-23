# Generated by Django 3.2.3 on 2021-05-23 13:33

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('community', '0002_alter_review_user_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='user_like',
            field=models.ManyToManyField(related_name='review_like', to=settings.AUTH_USER_MODEL),
        ),
    ]