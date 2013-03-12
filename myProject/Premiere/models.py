from django.db import models

class VimeoBasicModel(models.Model):
    user_id = models.CharField(primary_key=True,max_length=200, unique=True)
    name = models.CharField(max_length=500)
    url = models.CharField(max_length=500)
    paying = models.BooleanField()
    staffpicks = models.BooleanField()
    video = models.BooleanField()
    
    class Meta:
        db_table=u'vimeo_user_data'

    def __unicode__(self):
        return str(self.name)