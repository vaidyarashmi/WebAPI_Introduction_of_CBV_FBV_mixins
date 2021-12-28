from django.http import HttpResponse
import json
class HttpResMixins(object):
    def render_to_http_response(self,json_data):
        return HttpResponse(json_data,content_type='application/json')