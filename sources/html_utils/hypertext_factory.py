from utils import ComponentFactoryBase, HtmlBuilder, HtmlElement

class HyperTextFactory(ComponentFactoryBase):
    def __init__(self, VDOM_text): 
        self.object = VDOM_hypertext

    def create(self):
        if self.nostyle == "2":
            return self.htmlcode if self.visible != "0" else "<span style=\"display:none;\">%s</span>" % self.htmlcode

        if self.nostyle == "1":
            return "<span id=\"%s\" style=\"%s\">%s</span>" % (id, 'display:block;' if self.visible != "0" else 'display:none;', self.htmlcode)

        builder = HtmlBuilder()
        id = 'o_' + (self.id).replace('-', '_')
        builder.with_tag('div' if self.nostyle != "1" else 'span')
        builder.with_class_name(self.classname)
        builder.add_attribute('id', id)
        self._set_position(builder, self.top, self.left)
        self._set_visibility(builder, self.visible == '0')
        self._set_zindex(builder, self.zindex)
        self._set_size(builder, self.width, self.height if int("0%s" % self.height) > 0 else None)
        
        overflow_settings = {"1": 'hidden', "2": 'scroll', "3": 'visible'}
        builder.add_style('overflow', overflow_settings.get(self.overflow, 'auto'))

        builder.add_children_element(self.htmlcode)
        
        return builder.build().render()