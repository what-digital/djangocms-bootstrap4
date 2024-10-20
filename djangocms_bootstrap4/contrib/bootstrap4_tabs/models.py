from django.db import models
from django.utils.translation import gettext_lazy as _

from cms.models import CMSPlugin

from djangocms_bootstrap4.fields import AttributesField, TagTypeField

from .constants import (
    TAB_ALIGNMENT_CHOICES, TAB_EFFECT_CHOICES, TAB_TEMPLATE_CHOICES,
    TAB_TYPE_CHOICES,
)


class Bootstrap4Tab(CMSPlugin):
    """
    Components > "Navs - Tab" Plugin
    https://getbootstrap.com/docs/4.0/components/navs/
    """
    template = models.CharField(
        verbose_name=_('Template'),
        choices=TAB_TEMPLATE_CHOICES,
        default=TAB_TEMPLATE_CHOICES[0][0],
        max_length=255,
        help_text=_('This is the template that will be used for the component.'),
    )
    tab_type = models.CharField(
        verbose_name=_('Type'),
        choices=TAB_TYPE_CHOICES,
        default=TAB_TYPE_CHOICES[0][0],
        max_length=255,
    )
    tab_alignment = models.CharField(
        verbose_name=_('Alignment'),
        choices=TAB_ALIGNMENT_CHOICES,
        blank=True,
        max_length=255,
    )
    tab_index = models.PositiveIntegerField(
        verbose_name=_('Index'),
        null=True,
        blank=True,
        help_text=_('Index of element to open on page load starting at 1.'),
    )
    tab_effect = models.CharField(
        verbose_name=_('Animation effect'),
        choices=TAB_EFFECT_CHOICES,
        blank=True,
        max_length=255,
    )
    tag_type = TagTypeField()
    attributes = AttributesField()

    def __str__(self):
        return str(self.pk)

    def get_short_description(self):
        text = f'({self.tab_type})'

        if self.tab_alignment:
            text += f' .{self.tab_alignment}'
        return text


class Bootstrap4TabItem(CMSPlugin):
    """
    Components > "Navs - Tab Item" Plugin
    https://getbootstrap.com/docs/4.0/components/navs/
    """
    tab_title = models.CharField(
        verbose_name=_('Tab title'),
        max_length=255,
    )
    tag_type = TagTypeField()
    attributes = AttributesField()

    def __str__(self):
        return str(self.pk)

    def get_short_description(self):
        return self.tab_title
