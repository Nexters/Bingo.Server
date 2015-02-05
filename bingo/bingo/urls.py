from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bingo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^food_manager/', include('FoodManager.urls', namespace='food_manager')),
    url(r'^bingo_api/', include('BingoAPI.urls', namespace='bingo_api')),
)
