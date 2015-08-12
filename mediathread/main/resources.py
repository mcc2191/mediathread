from tastypie.authorization import Authorization
from tastypie.resources import Resource


class ApiKeysResource(Resource):
    class Meta:
        resource_name = 'apikeys'
        list_allowed_methods = ['get']
        object_class = {}
        authorization = Authorization()

    def detail_uri_kwargs(self, bundle_or_obj):
        return {}

    def get_object_list(self, request):
        return []

    def obj_get_list(self, bundle, **kwargs):
        return []

    def obj_get(self, bundle, **kwargs):
        return {}

    # if getattr(settings, 'DJANGOSHERD_FLICKR_APIKEY', None):
    #     context['apikey']['flickr_apikey'] = \
    #          settings.DJANGOSHERD_FLICKR_APIKEY

    # if getattr(settings, 'DJANGOSHERD_YOUTUBE_APIKEY', None):
    #     context['apikey']['youtube_apikey'] = \
    #         settings.DJANGOSHERD_YOUTUBE_APIKEY

    # return context
