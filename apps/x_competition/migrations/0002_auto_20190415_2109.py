# Generated by Django 2.1.7 on 2019-04-15 21:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('x_competition', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='competitionprofile',
            options={'verbose_name': '比赛设置', 'verbose_name_plural': '比赛设置'},
        ),
        migrations.RenameField(
            model_name='competitionprofile',
            old_name='competition_chioicenum',
            new_name='competition_choicenum',
        ),
    ]
