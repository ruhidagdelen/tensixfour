from django.db import models
from django.utils import timezone


class Post(models.Model):
	author = models.ForeignKey('auth.User')
	header = models.CharField(max_length=200)
	text = models.TextField()
	create_date = models.DateTimeField(default=timezone.now())
	pub_date = models.DateTimeField(null=True, blank=True)

	def publish(self):
		self.pub_date=timezone.now()
		self.save()

	def __str__(self):
		return self.header