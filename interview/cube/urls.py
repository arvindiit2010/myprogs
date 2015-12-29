from django.conf.urls import url
from cube import views

urlpatterns = [
    url(r'^user/$', views.UserView.as_view()),
    url(r'^cube/$', views.CubeView.as_view()),
    url(r'^user/(?P<user_id>\d+)/cube/$', views.CubeView.as_view()),
    url(r'^user/(?P<user_id>\d+)/cube/(?P<cube_id>\d+)/$', views.CubeView.as_view()), #for delete
    url(r'^user/(?P<user_id>\d+)/content/$', views.ContentView.as_view()),
    url(r'^user/(?P<user_id>\d+)/cube/(?P<cube_id>\d+)/content/$', views.AddContentToCubeView.as_view()),
    url(r'^user/(?P<user_id>\d+)/cube/(?P<cube_id>\d+)/content/(?P<content_id>\d+)/$', views.AddContentToCubeView.as_view()),
    url(r'^user/(?P<user_id>\d+)/cube/(?P<cube_id>\d+)/share/$', views.ShareCubeWithUserView.as_view()),
    url(r'^user/(?P<user_id>\d+)/content/(?P<content_id>\d+)/share/$', views.ShareContentWithUserView.as_view())
    #url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
]