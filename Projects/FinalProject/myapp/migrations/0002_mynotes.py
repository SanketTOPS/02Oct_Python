# Generated by Django 4.1 on 2025-01-17 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='mynotes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=100)),
                ('opt', models.CharField(max_length=100)),
                ('myfile', models.FileField(upload_to='MyNotes')),
                ('desc', models.TextField()),
            ],
        ),
    ]
