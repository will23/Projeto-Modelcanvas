# -*- encoding: utf-8 -*-
from django.conf import settings
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'modelcanvas.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.STATIC_ROOT}),

    url(r'^$', 'main.views.home', name='home'),
    url(r'^novo_negocio/$', 'main.views.novo_negocio', name='novo_negocio'),
    url(r'^listar_negocio/$', 'main.views.listar_negocio', name='listar_negocio'),
    url(r'^exibir_negocio/(?P<nid>\d+)/$', 'main.views.exibir_negocio', name='exibir_negocio'),
    url(r'^editar_negocio/(?P<nid>\d+)/$', 'main.views.editar_negocio', name='editar_negocio'),
    url(r'^excluir_negocio/(?P<nid>\d+)/$', 'main.views.excluir_negocio', name='excluir_negocio'),

    url(r'^teste/$', 'main.views.teste', name='teste'),
)
