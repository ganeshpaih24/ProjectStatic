# Generated by Django 4.0.2 on 2022-02-16 02:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_maininfo_des_alter_maininfo_hero_img_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.maininfo'),
        ),
    ]