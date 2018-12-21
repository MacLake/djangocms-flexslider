from ckeditor.fields import RichTextField
from cms.models import CMSPlugin
from django.db import models
from django.utils.translation import ugettext as _
from filer.fields.image import FilerImageField


class Slider(CMSPlugin):
	"""Flexslider"""
	width = models.PositiveSmallIntegerField(null=True, blank=True)
	UNITS = [
		('%', '%'),
		('px', 'px'),
		('em', 'em'),
		('rem', 'rem'),
	]
	unit = models.CharField(max_length=3, choices=UNITS, default='%')
	ANIMATIONS = [
		('fade', _('fade')),
		('slide', _('slide'))
	]
	animation = models.CharField(max_length=5, choices=ANIMATIONS, default='fade')
	slideshow_speed = models.PositiveSmallIntegerField(
		default=7000,
		verbose_name=_('slide show speed in ms'),
	)
	animation_speed = models.PositiveSmallIntegerField(
		default=600,
		verbose_name=_('animation speed in ms'),
	)
	randomize = models.BooleanField(default=False)
	control_nav = models.BooleanField(default=True)
	pause_on_action = models.BooleanField(default=False)
	pause_on_hover = models.BooleanField(default=True)
	
	# More possible options: see https://github.com/woocommerce/FlexSlider/wiki/FlexSlider-Properties
	def __str__(self):
		return ''


class Slide(CMSPlugin):
	"""Slide for Flexslider"""
	image = FilerImageField(verbose_name=_('slide image'))
	caption = RichTextField(blank=True, verbose_name=_('caption'))
	
	def __str__(self):
		return self.image.name or self.caption[:30]
