from utils import ComponentFactoryBase, HtmlBuilder, HtmlElement

class RichTextFactory(ComponentFactoryBase):
    def __init__(self, VDOM_richtext): 
        self.object = VDOM_richtext

    def create(self):
        builder = HtmlBuilder()
        id = 'o_' + (self.object.id).replace('-', '_')
        builder.with_tag('div')
        builder.with_class_name(self.object.classname)
        builder.add_attribute('id', id)
        self._set_position(builder, self.object.top, self.object.left)
        self._set_visibility(builder, self.object.visible == '0')
        self._set_zindex(builder, self.object.zindex)
        self._set_size(builder, self.object.width, self.object.height if self.object.height != "" and self.object.height != "0" else None)

        overflow_settings = {"1": 'hidden', "2": 'scroll', "3": 'visible'}
        builder.add_style('overflow', overflow_settings.get(self.object.overflow, 'auto'))
        builder.add_style('text-align', self.object.align if self.object.align != "" else None)
        builder.add_style('color', '#%s' % self.object.color if self.object.color != "" else None)
        builder.add_style('font', self.object.font.replace('"', "'") if self.object.font != "" else None)
        builder.add_style('text-decoration', 'underline' if self.object.underlined == "1" else 'line-through' if self.object.strikethrough == "1" else None)

        builder.add_children_element(self.object.value)
        
        return builder.build().render()