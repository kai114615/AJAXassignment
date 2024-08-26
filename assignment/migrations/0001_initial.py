# Generated by Django 5.1 on 2024-08-26 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('todo_id', models.AutoField(primary_key=True, serialize=False)),
                ('completed', models.BooleanField()),
                ('todo', models.CharField(max_length=100)),
                ('last_uplate', models.DateTimeField()),
            ],
            options={
                'db_table': 'Todo',
            },
        ),
    ]
