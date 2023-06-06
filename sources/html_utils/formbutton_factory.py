from utils import ComponentFactoryBase, HtmlBuilder, HtmlElement

class FormButtonFactory(ComponentFactoryBase):
    def __init__(self, VDOM_formbutton):
        ComponentFactoryBase.__init__(self)
        self.object = VDOM_formbutton

    def create(self):
        builder = HtmlBuilder()
        builder.with_tag("input")
        builder.with_class_name(self.object.classname)
        builder.add_attribute("id", self.object.id)

        types = ["submit", "reset", "button"]
        builder.add_attribute("type", types[self.object.type])
        
        builder.add_attribute("tabindex", self.object.tabindex)
        builder.add_attribute("value", self.object.label)
        builder.add_attribute("name", self.object.name)
        
        self._set_visibility(builder, self.object.visible == '0')
        self._set_position(builder, self.object.top, self.object.left)
        self._set_zindex(builder, self.object.zindex)
        self._set_size(builder, self.object.width, self.object.height)
        self._set_font(builder, self.object.fontsize, self.object.fontfamily, self.object.fontweight == 'bold', self.object.fontstyle == 'italic')

        return builder.build().render()