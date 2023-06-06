from utils import ComponentFactoryBase, HtmlBuilder, HtmlElement

class HyperTextFactory(ComponentFactoryBase):
    def __init__(self, VDOM_hypertext): 
        self.object = VDOM_hypertext

    def create(self):
        if self.object.nostyle == "2":
            return self.object.htmlcode

        if self.object.nostyle == "1":
            return "<span id=\"%s\">%s</span>" % (id, self.object.htmlcode)

        builder = HtmlBuilder()
        id = 'o_' + (self.object.id).replace('-', '_')
        builder.with_tag('div' if self.object.nostyle != "1" else 'span')
        builder.with_class_name(self.object.classname)
        builder.add_attribute('id', id)
        self._set_position(builder, self.object.top, self.object.left)
        self._set_visibility(builder, self.object.visible == '0')
        self._set_zindex(builder, self.object.zindex)
        self._set_size(builder, self.object.width, self.object.height if int("0%s" % self.object.height) > 0 else None)

        overflow_settings = {"1": 'hidden', "2": 'scroll', "3": 'visible'}
        builder.add_style('overflow', overflow_settings.get(self.object.overflow, 'auto'))

        builder.add_children_element(self.object.htmlcode)
        
        return builder.build().render()