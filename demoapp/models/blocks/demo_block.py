from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock

class DemoBlock(blocks.StructBlock):
    """
    wagtailのカスタムブロックのデモクラス
    """

    title = blocks.CharBlock(required=True, help_text="タイトル", verbose_name="タイトル")
    content = blocks.RichTextBlock(required=True, help_text="コンテンツ", verbose_name="コンテンツ")
    image = ImageChooserBlock(required=False, help_text="画像", verbose_name="画像")

    class Meta:
        template = "demoapp/blocks/demo_block.html"
        icon = "placeholder"
        label = "Demo Block"