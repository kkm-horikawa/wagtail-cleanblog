from wagtail.models import Page


class DemoPage(Page):
    """
    A simple demo page model for Wagtail CMS.
    """

    template = "demoapp/pages/demo_page.html"

