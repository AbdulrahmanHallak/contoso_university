# Generated by Django 4.2.17 on 2024-12-29 20:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_course_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='officeassignment',
            name='instructor',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='office', serialize=False, to='api.instructor'),
        ),
    ]
