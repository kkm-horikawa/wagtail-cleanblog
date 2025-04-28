from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock


class DemoBlock(blocks.StructBlock):
    """
    デモブロック
    """

    image = ImageChooserBlock(required=True)
    
    class Meta:
        template = "demoapp/blocks/demo_block.html"
        icon = "placeholder"
        label = "デモブロック"
        help_text = "画像表示を確認する簡易的なブロックです"