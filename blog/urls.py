from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static
from django.conf import  settings
app_name = 'blog'
urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', login_required(views.PostDetailView.as_view()), name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.ArchivesView.as_view(), name='archives'),
    # url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.CategoryView.as_view(), name='category'),
    url(r'^tag/(?P<pk>[0-9]+)/$', views.TagView.as_view(), name='tag'),
    url(r'^create/$', login_required(views.create), name='create'),
    url(r'^create_post/(?P<user_pk>[0-9]+)/$', views.create_post, name='create_post'),
    url(r'^user/profile/(?P<user_pk>[0-9]+)/$', login_required(views.user_profile), name='user_profile'),
    url(r'^user/img/(?P<user_pk>[0-9]+)/$', login_required(views.user_img), name='user_img'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)