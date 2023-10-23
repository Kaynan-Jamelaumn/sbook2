# Generated by Django 4.2.6 on 2023-10-23 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='gender',
            field=models.CharField(blank=True, choices=[('Woman', 'Woman'), ('Man', 'Man'), ('Non-binary', 'Non-binary'), ('Other', 'Other'), ('Genderfluid', 'Genderfluid'), ('Agender', 'Agender'), ('The Love of Your Life', 'The Love of Your Life'), ('Heavenly Demon', 'Heavenly Demon')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='sex',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True),
        ),
    ]
