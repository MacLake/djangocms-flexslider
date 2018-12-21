import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="djangocms_flexslider",
    version="0.5.2",
    author="Jens-Erik Weber",
    author_email="mail@passiv.de",
    description="Flexslider plug-in for Django CMS",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MacLake/djangocms-flexslider",
	packages=setuptools.find_packages(),
	include_package_data=True,
    install_requires=[
		"Django>=1.11",
		"django-cms>=3.4",
		"django-ckeditor",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Content Management System",
    ],
)
