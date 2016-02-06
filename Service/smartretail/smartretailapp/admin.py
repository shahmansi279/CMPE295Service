
from django.contrib import admin
from smartretailapp.models import NProduct, NProductClass,NOffers,NProdStore,NSensors,NCustomer,NStore,NSalesFact1997,NAisle,NTimeByDay


# Register your models here.


class CategoryAdmin(admin.ModelAdmin):

    pass


class ProductAdmin(admin.ModelAdmin):

    pass

class AisleAdmin(admin.ModelAdmin):

    pass


class OfferAdmin(admin.ModelAdmin):

    pass


class StoreAdmin(admin.ModelAdmin):

    pass


class ProductStoreAdmin(admin.ModelAdmin):

    pass

class SensorAdmin(admin.ModelAdmin):

    pass


class CustomerAdmin(admin.ModelAdmin):

    pass

class SalesFactAdmin(admin.ModelAdmin):

    pass




admin.site.register(NProductClass,CategoryAdmin)
admin.site.register(NProduct,ProductAdmin)
admin.site.register(NAisle,AisleAdmin)
admin.site.register(NStore,StoreAdmin)
admin.site.register(NCustomer,CustomerAdmin)
admin.site.register(NOffers,OfferAdmin)
admin.site.register(NProdStore,ProductStoreAdmin)
admin.site.register(NSensors,SensorAdmin)
admin.site.register(NSalesFact1997,SalesFactAdmin)