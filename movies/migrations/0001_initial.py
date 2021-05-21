# Generated by Django 3.2.3 on 2021-05-21 04:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('poster_path', models.CharField(max_length=200)),
                ('director', models.CharField(max_length=50)),
                ('runtiem', models.IntegerField()),
                ('age_rate', models.IntegerField()),
                ('main_actor', models.CharField(max_length=50)),
                ('genre', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
                ('release_year', models.IntegerField()),
                ('overview', models.TextField()),
                ('later', models.ManyToManyField(related_name='_movies_movie_later_+', to='movies.Movie')),
                ('series', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.series')),
            ],
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('img_path', models.CharField(max_length=100)),
                ('series', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.series')),
            ],
        ),
    ]