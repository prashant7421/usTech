# Generated by Django 3.0.5 on 2020-05-03 08:20

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(default='', max_length=20)),
                ('match_date', models.DateTimeField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MatchPlayers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.ProtectedError, to='cricket.Match', verbose_name='Select Match')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(default='', max_length=20)),
                ('image', models.ImageField(blank=True, upload_to='players/')),
                ('jersey_no', models.IntegerField(blank=True)),
                ('country', django_countries.fields.CountryField(max_length=2)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('logo', models.ImageField(blank=True, upload_to='team_logo/')),
                ('club_or_state', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PlayerStatistics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('run', models.IntegerField(default=0)),
                ('wickets', models.IntegerField(default=0)),
                ('catches', models.IntegerField(default=0)),
                ('batting_over', models.FloatField(default=0.0)),
                ('bowling_over', models.IntegerField(default=0)),
                ('match_player', models.OneToOneField(on_delete=django.db.models.deletion.ProtectedError, to='cricket.MatchPlayers', verbose_name='Select Player')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='matchplayers',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.ProtectedError, to='cricket.Player', verbose_name='Select Player'),
        ),
        migrations.AddField(
            model_name='matchplayers',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.ProtectedError, to='cricket.Team', verbose_name='Select Team'),
        ),
        migrations.AddField(
            model_name='match',
            name='team1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.ProtectedError, related_name='team1', to='cricket.Team', verbose_name='Select Team 1'),
        ),
        migrations.AddField(
            model_name='match',
            name='team2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.ProtectedError, related_name='team2', to='cricket.Team', verbose_name='Select Team 2'),
        ),
        migrations.AlterUniqueTogether(
            name='matchplayers',
            unique_together={('match', 'team', 'player')},
        ),
    ]
