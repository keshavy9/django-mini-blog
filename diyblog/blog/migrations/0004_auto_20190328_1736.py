# Generated by Django 2.1.7 on 2019-03-28 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.TextField(help_text='Enter a title for the blog post', max_length='30', null=True),
        ),
    ]
