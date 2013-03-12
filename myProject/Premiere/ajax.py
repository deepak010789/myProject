from django.utils import simplejson
from dajaxice.decorators import dajaxice_register
from myProject.Premiere.models import VimeoBasicModel

@dajaxice_register
def filter(request, value=None, id=None):
    if value:
        vimeo_objects = VimeoBasicModel.objects.filter(name__istartswith=value)
    else:
        vimeo_objects = VimeoBasicModel.objects.none()
    count = vimeo_objects.count()
    if count>100:
        vimeo_objects = vimeo_objects[0:100]
    objects = []
    for obj in vimeo_objects:
        per_obj_list = []
        per_obj_list.append(obj.name)
        per_obj_list.append(obj.paying)
        per_obj_list.append(obj.staffpicks)
        per_obj_list.append(obj.video)
        
        objects.append(per_obj_list)
    return simplejson.dumps({'objects': objects, 'count':count ,'id':id})