from django import template

register = template.Library()


@register.filter
def bool_js(value):
	"""Convert Python Boolean to JavasScript"""
	return 'true' if value else 'false'
