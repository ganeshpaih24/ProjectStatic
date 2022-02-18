# Generated by Django 4.0.2 on 2022-02-08 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='genere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='mainInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('catgry', models.CharField(choices=[('Anime', 'Anime'), ('Drama', 'Drama'), ('Web-Series', 'Web-Series'), ('Movies', 'Movies')], max_length=50, null=True)),
                ('post_img', models.URLField()),
                ('hero_img', models.URLField()),
                ('generes', models.ManyToManyField(to='app.genere')),
            ],
        ),
    ]
