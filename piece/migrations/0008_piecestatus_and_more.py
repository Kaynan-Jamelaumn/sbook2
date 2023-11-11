# Generated by Django 4.2.6 on 2023-11-11 00:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('piece', '0007_pieceanotation_unique_piece_anotation_for_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='PieceStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Finished', 'Finished'), ('Abandoned', 'Abandoned'), ('In Progress', 'In Progress'), ('Paused', 'Paused'), ('Hoping to Start', 'Hoping to Start')], max_length=20)),
                ('ratimg', models.FloatField(choices=[(0.5, '0.5'), (1.0, '1.0'), (1.5, '1.5'), (2.0, '2.0'), (2.5, '2.5'), (3.0, '3.0'), (3.5, '3.5'), (4.0, '4.0'), (4.5, '4.5'), (5.0, '5.0')])),
                ('summary', models.TextField(blank=True, max_length=3000, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveConstraint(
            model_name='pieceanotation',
            name='unique_piece_anotation_for_user',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='piece',
        ),
        migrations.RemoveField(
            model_name='pieceanotation',
            name='piece',
        ),
        migrations.RemoveField(
            model_name='pieceanotation',
            name='status',
        ),
        migrations.AddField(
            model_name='pieceanotation',
            name='chapter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='piece_annotations', to='piece.chapter'),
        ),
        migrations.AddField(
            model_name='pieceanotation',
            name='page',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='piece_annotations', to='piece.page'),
        ),
        migrations.AddConstraint(
            model_name='pieceanotation',
            constraint=models.CheckConstraint(check=models.Q(('chapter__isnull', False), ('page__isnull', False), _connector='OR'), name='chapter_or_page_required'),
        ),
        migrations.AddField(
            model_name='piecestatus',
            name='piece',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='piece.piece'),
        ),
        migrations.AddField(
            model_name='piecestatus',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
