from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext as _

from djangocms_flexslider.models import Slider, Slide


@plugin_pool.register_plugin
class SliderPublisher(CMSPluginBase):
	"""Flexslider"""
	model = Slider
	module = 'Flexslider'
	name = _('Slider')
	render_template = 'djangcms_flexslider/slider.html'
	allow_children = True
	child_classes = ['SlidePublisher']
	
	def render(self, context, instance, placeholder):
		context.update({'instance': instance})
		return context


@plugin_pool.register_plugin
class SlidePublisher(CMSPluginBase):
	"""Slide for Flexslider"""
	model = Slide
	module = 'Flexslider'
	name = _('Slide')
	render_template = 'djangcms_flexslider/slide.html'
	require_parent = True
	parent_classes = ['SliderPublisher']
	allow_children = False
	
	def render(self, context, instance, placeholder):
		context.update({'instance': instance})
		return context
