# djangocms-flexslider
Flexslider plug-in for [Django CMS](https://www.django-cms.org/)

Based on [FlexSlider](http://www.woocommerce.com/flexslider/),
[Git repository](https://github.com/woocommerce/FlexSlider)

You need django-ckeditor (different from djangocms_text_ckeditor), add

```
'ckeditor',
```

to INSTALLED_APPS in your Django settings.

You need to make sure that jQuery in a version compatible with FlexSlider, i .e. >= 1.7.0, is included in your templates.
