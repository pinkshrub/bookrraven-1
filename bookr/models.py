from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Artist(models.Model):
	artist_name = models.CharField(max_length=100)
	site = models.URLField(max_length=200)
	sound = models.URLField(max_length=200)
	artist_photo = models.ImageField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	contact_id = models.ForeignKey(User)
	def __str__(self):
		return 'ID: %s | Artist: %s | Main Contact: %s' % (self.id, self.artist_name, self.contact_id.email)

class Venue(models.Model):
	SEATTLE = 'SEA'
	SAN_FRANCISCO = 'SFO'
	CITY_CHOICES = (
		(SEATTLE, 'Seattle'),
		(SAN_FRANCISCO, 'San Francisco')
		)
	WASHINGTON = 'WA'
	CALIFORNIA = 'CA'
	STATE_CHOICES = (
		(WASHINGTON, 'Washington'),
		(CALIFORNIA, 'California')
		)
	venue_name = models.CharField(max_length=100)
	address = models.CharField(max_length=100)
	city = models.CharField(max_length=45, choices=CITY_CHOICES)
	state= models.CharField(max_length=2, choices=STATE_CHOICES)
	zipcode = models.CharField(max_length=5)
	venue_phone = models.CharField(max_length=10)
	venue_photo = models.ImageField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	booker_id = models.ForeignKey(User)

class Event(models.Model):
	PENDING = 'Pend'
	ACCEPTED = 'Acpt'
	DECLINED = 'Decl'
	STATUS_CHOICES = (
		(PENDING, 'Pending Event'),
		(ACCEPTED, 'Accepted Event'),
		(DECLINED, 'Declined Event')
		)
	event_date = models.DateTimeField()
	status = models.CharField(max_length=45, choices=STATUS_CHOICES, default=PENDING)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	venue_id = models.ForeignKey('Venue')
	artist_id = models.ForeignKey('Artist')

class Message(models.Model):
	message = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	event_id = models.ForeignKey('Event')	
	author_id = models.ForeignKey(User)

class Comment(models.Model):
	comment = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	message_id = models.ForeignKey('Message')	
	event_id = models.ForeignKey('Event')
	author_id = models.ForeignKey(User)