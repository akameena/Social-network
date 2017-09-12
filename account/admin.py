from django.contrib import admin
from account.models import UserProfile
# Register your models here.
#admin.site.site_header = "Administration"   # we can change aadmin heading like this
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('User', 'city','mobile_no','website','user_info') #this class show all model atribute show on user profile admin

    def user_info(self,obj): #method use for define new name description to user_info
        return obj.description
    
    def get_queryset(self,request):# this method overreide the query_set method
        #in super class and work for ordering of disply data ilist display
        queryset = super(UserProfileAdmin,self).get_queryset(request)
        queryset = queryset.order_by('mobile_no','User')
        return queryset

    user_info.short_description = 'INFO' #use for to shoe user_info in short form INFO
admin.site.register(UserProfile,UserProfileAdmin)
