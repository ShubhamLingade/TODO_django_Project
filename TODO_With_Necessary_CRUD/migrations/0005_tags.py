# Generated by Django 3.2.11 on 2022-02-27 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TODO_With_Necessary_CRUD', '0004_alter_custem_custem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tags', models.CharField(max_length=30)),
            ],
        ),
    ]
