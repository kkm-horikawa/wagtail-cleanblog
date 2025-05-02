from wagtail.models import Page
from wagtail.api import APIField  # apiを有効にするためのインポート
from wagtail.admin.panels import FieldPanel
from django.db import models


class DemoPage(Page):
    """
    デモページモデル
    """

    template = "demoapp/pages/demo_page.html"

    content = models.CharField()
    
    # apiを有効にするフィールドを指定
    # これにより、APIからこのフィールドにアクセスできるようになります
    api_fields = [
        APIField("content"),
    ]

    content_panels = Page.content_panels + [
        FieldPanel("content"),
    ]
    
    class Meta:
        verbose_name = "Demo Page"
        verbose_name_plural = "Demo Pages"
