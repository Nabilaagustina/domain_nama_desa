from django.shortcuts import render
from django.http import JsonResponse
from .models import Provinsi, Kabupaten, Kecamatan, Desa, DomainDesa

def form_domain(request):
    provinsi = Provinsi.objects.all()
    return render(request, 'form_domain.html', {'provinsi': provinsi})

def get_kabupaten(request):
    provinsi_id = request.GET.get('provinsi_id')
    kabupaten = Kabupaten.objects.filter(domainsdesa__kode_provinsi_id=provinsi_id).distinct()
    data = list(kabupaten.values('kode_kabupaten', 'nama'))
    return JsonResponse({'data': data})

def get_kecamatan(request):
    kabupaten_id = request.GET.get('kabupaten_id')
    kecamatan = Kecamatan.objects.filter(domainsdesa__kode_kabupaten_id=kabupaten_id).distinct()
    data = list(kecamatan.values('kode_kecamatan', 'nama'))
    return JsonResponse({'data': data})

def get_desa(request):
    kecamatan_id = request.GET.get('kecamatan_id')
    desa = Desa.objects.filter(domainsdesa__kode_kecamatan_id=kecamatan_id).distinct()
    data = list(desa.values('kode_desa', 'nama'))
    return JsonResponse({'data': data})

def get_domain(request):
    desa_id = request.GET.get('desa_id')
    domain_obj = DomainDesa.objects.filter(kode_desa_id=desa_id).first()
    domain_name = domain_obj.nama_domain if domain_obj else "-"
    return JsonResponse({'nama_domain': domain_name})
