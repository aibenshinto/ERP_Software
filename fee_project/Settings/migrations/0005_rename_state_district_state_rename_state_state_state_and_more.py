# Generated by Django 4.2.5 on 2023-09-26 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Settings', '0004_rename_type_masterdata_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='district',
            old_name='State',
            new_name='state',
        ),
        migrations.RenameField(
            model_name='state',
            old_name='State',
            new_name='state',
        ),
        migrations.RemoveField(
            model_name='district',
            name='District',
        ),
        migrations.AddField(
            model_name='district',
            name='district',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]