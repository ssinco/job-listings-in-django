# Generated by Django 5.0.6 on 2024-06-26 05:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_profile_profile_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('about', models.TextField(max_length=250)),
                ('location', models.CharField(max_length=60)),
                ('employee_count', models.CharField(choices=[('0 - 10', '0 - 10'), ('10 - 50', '10 - 50'), ('50 - 250', '50 - 250'), ('250 - 1000', '250 - 1000'), ('1000+', '1000+')], default='0 - 10', max_length=20)),
                ('industry', models.CharField(choices=[('Finance', 'Finance'), ('Software', 'Software'), ('Healthcare', 'Healthcare')], default='Finance', max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='jobhistory',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main_app.company'),
        ),
    ]