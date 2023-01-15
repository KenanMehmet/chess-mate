# Generated by Django 4.1.1 on 2023-01-15 18:31

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forename', models.CharField(max_length=32)),
                ('surname', models.CharField(max_length=32)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64)),
                ('email', models.CharField(max_length=256)),
                ('password', models.CharField(max_length=256)),
                ('rating', models.IntegerField(default=800)),
                ('nationality', django_countries.fields.CountryField(max_length=2)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.IntegerField(choices=[(0, 'tie'), (1, 'white'), (2, 'black')])),
                ('ranked', models.BooleanField()),
                ('black_player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='black_player', to='chess.player')),
                ('white_player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='white_player', to='chess.player')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chess.author')),
                ('tags', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chess.tag')),
            ],
        ),
    ]
