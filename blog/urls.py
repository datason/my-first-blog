from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/new/', views.post_new, name='post_new'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    path('post/<pk>/publish/', views.post_publish, name='post_publish'),
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
    path('post/<int:pk>/preference/<int:userpreference>/', views.postpreference,  name='postpreference'),
    # path('post/<pk>/preference/<int:userpreference>/', views.postpreference,  name='postpreference'),
    # path('post/<int:pk>/preference/<userpreference>/', views.postpreference,  name='postpreference'),
    # path('post/<pk>/preference/<userpreference>/', views.postpreference,  name='postpreference'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns = [
#      url(r'^(?P<pk>\d+)/preference/(?P<userpreference>\d+)/$', views.postpreference, name='postpreference'),
# ]

# urlpatterns += [
        # url(r'^(?P<pk>\d+)/preference/(?P<userpreference>\d+)/$', views.postpreference, name='postpreference'),
    # url('post/<int:pk>/preference/<userpreference>', views.postpreference, name='postpreference'),
# ]
# if settings.DEBUG:

# urlpatterns += url(r'^(?P<pk>\d+)/preference/(?P<userpreference>\d+)/$', postpreference, name='postpreference')