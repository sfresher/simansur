from django.contrib import admin
from MainApp.models import Surat, Disposisi, UserPencatatSurat, UserPenerimaSurat

class SuratAdmin(admin.ModelAdmin):
    list_display = ('no_surat', 'no_agenda', 'perihal_surat', 'tanggal_surat_masuk', 
                    'keterangan_disposisi', 'tingkat_kepentingan', 'dari', 
                    'timestamp_surat', 'id_penerima', 'id_pencatat')


class DisposisiAdmin(admin.ModelAdmin):
    list_display = ('id_penerima_disposisi', 'no_surat_disposisi', 'user_name_pengirim_disposisi', 
                    'catatan_tambahan', 'timestamp_disposisi', 'tanggal_surat_disposisi')
    
class UserPencatatSuratAdmin(admin.ModelAdmin):
    list_display = ('user', 'bidang', 'jabatan', 'role_pencatat')
    
class UserPenerimaSuratAdmin(admin.ModelAdmin):
    list_display = ('user', 'bidang', 'jabatan', 'no_telepon')

# Register your models here.
admin.site.register(Surat, SuratAdmin)
admin.site.register(Disposisi, DisposisiAdmin)
admin.site.register(UserPencatatSurat, UserPencatatSuratAdmin)
admin.site.register(UserPenerimaSurat, UserPenerimaSuratAdmin)

