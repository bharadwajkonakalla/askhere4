# Generated by Django 2.2.7 on 2020-06-17 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Ask', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='interest',
            name='user_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Ask.UserLogin'),
            preserve_default=False,
        ),
    ]