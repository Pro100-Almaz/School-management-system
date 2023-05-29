# Generated by Django 3.2.17 on 2023-05-29 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0005_auto_20230530_0053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='prerequisites',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='course_prerequisites', to='document.course'),
        ),
    ]
