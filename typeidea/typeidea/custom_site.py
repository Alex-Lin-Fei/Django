from django.contrib.admin import AdminSite


class CustomSite(AdminSite):
    site_header = 'Typeidea'
    site_title = 'Typeidea Management System'
    index_title = 'HomePage'


custom_site = CustomSite(name='cus_admin')