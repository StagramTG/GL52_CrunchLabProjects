# Generated by Django 2.2 on 2019-06-17 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userproject',
            name='user_role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='restapi.ProjectRoles'),
        ),
    ]