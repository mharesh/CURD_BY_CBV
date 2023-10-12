# Generated by Django 4.2.5 on 2023-10-09 06:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sname', models.CharField(max_length=100)),
                ('Sprin', models.CharField(max_length=100)),
                ('Sloc', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Stname', models.CharField(max_length=123)),
                ('Stage', models.IntegerField()),
                ('Sname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='app.school')),
            ],
        ),
    ]