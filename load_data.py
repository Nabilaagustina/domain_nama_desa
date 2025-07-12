import csv
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "domain_nama_desa.settings")
django.setup()

from rekomendasi.models import Provinsi, Kabupaten, Kecamatan, Desa, DomainDesa

def load_data():
    with open('provinsi.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            Provinsi.objects.get_or_create(
                kode_provinsi=row['KODE PROVINSI'],
                defaults={'nama': row['NAMA PROVINSI']}
            )
    
    with open('kabupaten.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            Kabupaten.objects.get_or_create(
                kode_kabupaten=row['KODE KABUPATEN'],
                defaults={'nama': row['NAMA KABUPATEN']}
            )
    
    with open('kecamatan.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            Kecamatan.objects.get_or_create(
                kode_kecamatan=row['KODE KECAMATAN'],
                defaults={'nama': row['NAMA KECAMATAN']}
            )
    
    with open('desa.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            Desa.objects.get_or_create(
                kode_desa=row['KODE DESA'],
                defaults={'nama': row['NAMA DESA']}
            )
    
    with open('domain_desa.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            desa = Desa.objects.get(kode_desa=row['KODE DESA'])
            prov = Provinsi.objects.get(kode_provinsi=row['KODE PROVINSI'])
            kab = Kabupaten.objects.get(kode_kabupaten=row['KODE KABUPATEN'])
            kec = Kecamatan.objects.get(kode_kecamatan=row['KODE KECAMATAN'])
            DomainDesa.objects.get_or_create(
                kode_desa=desa,
                kode_provinsi=prov,
                kode_kecamatan=kec,
                kode_kabupaten=kab,
                defaults={'nama_domain': row['NAMA DOMAIN']}
            )

load_data()
print('Data berhasil dimasukkan ke database Django 🎺')
