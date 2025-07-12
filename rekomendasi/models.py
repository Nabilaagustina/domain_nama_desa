from django.db import models

class Provinsi(models.Model):
    kode_provinsi = models.CharField(max_length=15, primary_key=True)
    nama = models.CharField(max_length=100)

    def __str__(self):
        return self.nama

class Kabupaten(models.Model):
    kode_kabupaten = models.CharField(max_length=15, primary_key=True)
    nama = models.CharField(max_length=100)

    def __str__(self):
        return self.nama

class Kecamatan(models.Model):
    kode_kecamatan = models.CharField(max_length=15, primary_key=True)
    nama = models.CharField(max_length=100)

    def __str__(self):
        return self.nama

class Desa(models.Model):
    kode_desa = models.CharField(max_length=15, primary_key=True)
    nama = models.CharField(max_length=100)

    def __str__(self):
        return self.nama

class DomainDesa(models.Model):
    kode_provinsi = models.ForeignKey(Provinsi, on_delete=models.CASCADE, related_name='domainsdesa')
    kode_kabupaten = models.ForeignKey(Kabupaten, on_delete=models.CASCADE, related_name='domainsdesa')
    kode_kecamatan = models.ForeignKey(Kecamatan, on_delete=models.CASCADE, related_name='domainsdesa')
    kode_desa = models.ForeignKey(Desa, on_delete=models.CASCADE, related_name='domainsdesa')
    nama_domain = models.CharField(max_length=250)

    def __str__(self):
        return self.nama_domain
