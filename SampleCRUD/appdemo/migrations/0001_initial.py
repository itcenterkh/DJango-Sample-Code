# Generated by Django 2.0 on 2018-01-26 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('ip', models.GenericIPAddressField()),
                ('order', models.IntegerField()),
            ],
        ),
    ]