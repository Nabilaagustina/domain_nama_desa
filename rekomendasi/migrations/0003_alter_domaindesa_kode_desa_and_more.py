# Generated by Django 5.2.4 on 2025-07-11 15:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rekomendasi', '0002_remove_domaindesa_kode_domain_domaindesa_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domaindesa',
            name='kode_desa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='domainsdesa', to='rekomendasi.desa'),
        ),
        migrations.AlterField(
            model_name='domaindesa',
            name='kode_kabupaten',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='domainsdesa', to='rekomendasi.kabupaten'),
        ),
        migrations.AlterField(
            model_name='domaindesa',
            name='kode_kecamatan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='domainsdesa', to='rekomendasi.kecamatan'),
        ),
        migrations.AlterField(
            model_name='domaindesa',
            name='kode_provinsi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='domainsdesa', to='rekomendasi.provinsi'),
        ),
    ]
