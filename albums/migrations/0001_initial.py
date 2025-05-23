# Generated by Django 4.1.7 on 2025-04-23 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='相册标题')),
                ('description', models.TextField(blank=True, null=True, verbose_name='描述')),
                ('is_public', models.BooleanField(default=False, verbose_name='是否公开')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '相册',
                'verbose_name_plural': '相册',
                'ordering': ['-created_at'],
            },
        ),
    ]
