from django.contrib import admin
from tendermanagement.models import *
# Register your models here.
admin.site.register(req_user)
admin.site.register(user_type)
admin.site.register(tender_type)
admin.site.register(category_type)
admin.site.register(t_request)
admin.site.register(bid_request)
admin.site.register(card_details)
admin.site.register(feedback)
admin.site.register(admin_users)