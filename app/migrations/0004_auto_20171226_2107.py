# Generated by Django 2.0 on 2017-12-26 21:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20171226_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preventivo',
            name='prestazione2',
            field=models.ForeignKey(blank=True, default='None', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prestazione2', to='app.Prestazione'),
        ),
        migrations.AlterField(
            model_name='preventivo',
            name='prestazione3',
            field=models.ForeignKey(blank=True, default='None', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prestazione3', to='app.Prestazione'),
        ),
        migrations.AlterField(
            model_name='preventivo',
            name='prestazione4',
            field=models.ForeignKey(blank=True, default='None', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prestazione4', to='app.Prestazione'),
        ),
        migrations.AlterField(
            model_name='preventivo',
            name='prestazione5',
            field=models.ForeignKey(blank=True, default='None', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prestazione5', to='app.Prestazione'),
        ),
    ]
