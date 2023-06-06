from utils import ComponentFactoryBase, HtmlBuilder, HtmlElement

class TextFactory(ComponentFactoryBase):
    def __init__(self, VDOM_text): 
        self.object = VDOM_text

    def create(self):
        print(test)
        builder = HtmlBuilder()

        self._set_position(builder, self.object.top, self.object.left)
        self._set_visibility(builder, self.object.visible == '0')
        self._set_zindex(builder, self.object.zindex)
        self._set_size(builder, self.object.width, None)
        self._set_font(builder, self.object.fontsize, self.object.fontfamily, self.object.fontweight == 'bold', self.object.fontstyle == 'italic')
        
        builder.with_tag(self.object.htmltag)
        builder.add_css('%s' % self.object.css if self.object.css else "")

        builder.add_style('overflow', 'auto')
        builder.add_style('text-align', self.object.align)
        builder.add_style('color', '#%s' % self.object.color if self.object.color else None)
        builder.add_style('text-decoration', self.object.textdecoration)
        builder.with_class_name(self.object.classname)
        builder.add_attribute('title', self.object.hint.replace('"', '&quot;'))
        builder.add_attribute('id', self.object.id_special)
        builder.add_attribute('debug_info', self.object.debug_info)

        return builder.build().render()
        