from wagtail.models import Page
from wagtail import fields
from wagtail.admin.panels import FieldPanel
from demoapp.models.blocks.demoblock import DemoBlock


class DemoPage(Page):
    """
    画像表示確認をするためのデモページ
    """

    template = "demoapp/pages/demo_page.html"

    contents = fields.StreamField(
        [
            ("demo_block", DemoBlock()),
        ],
        blank=True,
    )
    
    content_panels = Page.content_panels + [
        FieldPanel("contents"),
    ]
    
    class Meta:
        verbose_name = "デモページ"
        verbose_name_plural = "デモページ"
        ordering = ["-first_published_at"]