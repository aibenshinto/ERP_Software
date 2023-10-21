# Generated by Django 4.2.5 on 2023-09-22 07:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Settings', '0004_rename_type_masterdata_type'),
        ('Student', '0013_alter_studentform_feestype'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentform',
            name='payment_type',
            field=models.CharField(choices=[('one time', 'One Time '), ('2time', 'Two Time ')], default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='studentform',
            name='feestype',
            field=models.ForeignKey(choices=[('one time', 'One Time '), ('2time', 'Two Time ')], limit_choices_to={'type': 'Fee Type'}, on_delete=django.db.models.deletion.CASCADE, related_name='FeeStudents', to='Settings.masterdata', verbose_name='Installment Type'),
        ),
    ]