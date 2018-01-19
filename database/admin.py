from django.contrib import admin
from database.models import Presenter, Lecture, Feedback, Newsletter, Discipline, LecturesDiscipline, Event, SignUp, PagesContent, Gallery, Atmos,  AIC_Company, AIC_Discipline
class LectureAdmin(admin.ModelAdmin):
	list_display = ('id','presenter','topic','date')
	search_fields = ('id','topic',)
	list_filter = ('discipline','date','campus','allowed')
	date_hierarchy = 'date'
	raw_id_fields = ('presenter',)
	filter_horizontal = ('discipline',)
#	fields = get_vars(Lecture)
#	readonly_fields  = ('id',)
	
class NewsAdmin(admin.ModelAdmin):
	list_display = ('id','name', 'newsletter', 'allowed' )
	search_fields = ('id','name', 'newsletter', 'allowed')
	
class PresenterAdmin(admin.ModelAdmin):
	list_display = ('id','name' )
	search_fields = ('id','name')
	list_filter =('name',)
	
class FeedbackAdmin(admin.ModelAdmin):
	list_display = ('lecture', 'feedback', 'slides', 'video_link', 'poster')
	raw_id_fields = ('lecture', )
	search_fields = ('lecture', 'feedback', 'slides', 'video_link', 'poster')
	
class EventAdmin(admin.ModelAdmin):
	list_display = ('__str__','allowed')
	
class PageAdmin(admin.ModelAdmin):
	list_display = ('name','link','content')

class SignupAdmin(admin.ModelAdmin):
	list_display = ('first_name','last_name', 'email','talk_discipline', 'lect_topics')

class GalleryAdmin(admin.ModelAdmin):
        list_display = ('name','__str__','details','allowed')

class AtmosAdmin(admin.ModelAdmin):
	list_display = ('id','topic','date')
	search_fields = ('id','topic',)
	list_filter = ('discipline','date','campus')
	date_hierarchy = 'date'
	filter_horizontal = ('discipline',)

class AIC_Company_Admin(admin.ModelAdmin):
	list_display = ('id','company_name','submission_date')
	search_fields = ('id','comapny_name',)
	list_filter = ('discipline','submission_date')
	date_hierarchy = 'submission_date'
	filter_horizontal = ('discipline',)


admin.site.register(Presenter,PresenterAdmin)
admin.site.register(Lecture, LectureAdmin)
admin.site.register(Feedback,FeedbackAdmin)
admin.site.register(Newsletter,NewsAdmin)
admin.site.register(Discipline)
#admin.site.register(LecturesDiscipline)
admin.site.register(Gallery,GalleryAdmin)
admin.site.register(Event,EventAdmin)
admin.site.register(SignUp, SignupAdmin)
admin.site.register(PagesContent, PageAdmin)
admin.site.register(Atmos, AtmosAdmin)
admin.site.register(AIC_Discipline)
admin.site.register(AIC_Company, AIC_Company_Admin)
