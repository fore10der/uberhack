from django.db import models

class DataframeNode(models.Model):
	tiff_file = models.FileField(upload_to='dataframes/')
	gtiff_file = models.FileField(upload_to='dataframes/')