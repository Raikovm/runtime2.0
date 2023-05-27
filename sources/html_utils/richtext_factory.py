from utils import ComponentFactoryBase, HtmlBuilder, HtmlElement

class RichTextFactory(ComponentFactoryBase):
    def __init__(self, VDOM_richtext): 
        self.object = VDOM_richtext

    def create(self):
        builder = HtmlBuilder()
        id = 'o_' + (self.id).replace('-', '_')
        builder.with_tag('div')
        builder.with_class_name(self.classname)
        builder.add_attribute('id', id)
        self._set_position(builder, self.top, self.left)
        self._set_visibility(builder, self.visible == '0')
        self._set_zindex(builder, self.zindex)
        self._set_size(builder, self.width, self.height if self.height != "" and self.height != "0" else None)

        overflow_settings = {"1": 'hidden', "2": 'scroll', "3": 'visible'}
        builder.add_style('overflow', overflow_settings.get(self.overflow, 'auto'))
        builder.add_style('text-align', self.align if self.align != "" else None)
        builder.add_style('color', '#%s' % self.color if self.color != "" else None)
        builder.add_style('font', self.font.replace('"', "'") if self.font != "" else None)
        builder.add_style('text-decoration', 'underline' if self.underlined == "1" else 'line-through' if self.strikethrough == "1" else None)

        builder.add_children_element(self.value)
        
        return builder.build().render()