# Generated by Django 4.1.2 on 2022-10-29 23:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_comment_commenter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.listing')),
            ],
        ),
    ]
