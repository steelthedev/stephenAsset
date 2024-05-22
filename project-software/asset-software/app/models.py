from django.db import models


# Create your models here.

class Asset(models.Model):
    user = models.ForeignKey("account.Users", on_delete=models.CASCADE, related_name='asset_user', null=True, blank=True)
    asset_name = models.TextField()
    asset_id = models.CharField(max_length=200)
    assign_date = models.DateTimeField(verbose_name="assign date", auto_now_add=True)
    asset_image = models.ImageField(upload_to='picture')
    
    
    def __str__(self):
        return self.asset_name
