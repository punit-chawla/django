from django.conf.urls import url
from . import views
app_name = 'teachers'
urlpatterns = [
    url(r'^$',views.index,name='teachers'),
    #url(r'^(?s<student_id>[0-9]+)/$',views.detail,name="viewstudent"),
    url(r'^(?P<teacher_id>[0-9]+)/edit/$',views.edit,name="editteacher"),
	url(r'^(?P<teacher_id>[0-9]+)/update/$',views.update,name="updateteacher"),
	url(r'^(?P<teacher_id>[0-9]+)/delete/$',views.delete,name="deleteteacher"),
    url(r'^add',views.add,name="addteacher"),

]