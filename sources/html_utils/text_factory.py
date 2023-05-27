from utils import ComponentFactoryBase, HtmlBuilder, HtmlElement

class TextFactory(ComponentFactoryBase):
    def __init__(self, VDOM_text): 
        self.object = VDOM_text

    def create(self):
        builder = HtmlBuilder()

        self._set_position(builder, self.top, self.left)
        self._set_visibility(builder, self.visible == '0')
        self._set_zindex(builder, self.zindex)
        self._set_size(builder, self.width, None)
        self._set_font(builder, self.fontsize, self.fontfamily, self.fontweight == 'bold', self.fontstyle == 'italic')
        
        builder.with_tag(self.htmltag)
        builder.add_css('%s' % self.css if self.css else "")

        builder
            .add_style('overflow', 'auto')
            .add_style('text-align', self.align)
            .add_style('color', '#%s' % self.color if self.color else None)
            .add_style('text-decoration', self.textdecoration)
        builder
            .with_class_name(self.classname)
            .add_attribute('title', self.hint.replace('"', '&quot;'))
            .add_attribute('id', self.id_special)
        builder.add_attribute('debug_info', debug_info)

        return builder.build().render()
        