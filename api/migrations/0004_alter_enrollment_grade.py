# Generated by Django 4.2.17 on 2024-12-30 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_officeassignment_instructor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrollment',
            name='grade',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('F', 'F')], max_length=1, null=True),
        ),
    ]
