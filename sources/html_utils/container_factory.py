from utils import ComponentFactoryBase, HtmlBuilder, HtmlElement

class ContainerFactory(ComponentFactoryBase):
    def __init__(self, VDOM_container): 
        self.object = VDOM_container

    def create(self):
        builder = HtmlBuilder()

        if self.object.securitycode and session["SecurityCode"] and str(session["SecurityCode"]) in self.object.securitycode.split(";"):
            self.object.visible = "1"

        id = 'o_' + (self.object.id).replace('-', '_')

        builder.with_tag('div')
        builder.with_class_name(self.object.classname)
        builder.add_attribute('id', id)
        self._set_position(builder, self.object.top, self.object.left)
        self._set_visibility(builder, self.object.visible == '0')
        self._set_zindex(builder, self.object.zindex)

        overflow_settings = {"1": 'hidden', "2": 'scroll', "3": 'visible'}
        builder.add_style('overflow', overflow_settings.get(self.object.overflow, 'auto'))
        builder.add_style('height', "%spx" % self.object.height if self.object.heightauto == "0" else None)
        builder.add_style('background-color', '#%s' % self.object.backgroundcolor if self.object.backgroundcolor != "" else None)
        builder.add_style('background-image', "url('%s')" % id2link1(self.object.backgroundimage) if self.object.backgroundimage != "" else None)
        repeat_settings = {'1': 'no-repeat', '2': 'repeat-x', '3': 'repeat-y'}
        builder.add_style('background-repeat', repeat_settings.get(self.object.backgroundrepeat, None))

        builder.add_attribute('footer', 'footer' if self.object.footer == "1" else None)

        if self.object.titlewrap != "0":
            title_element = HtmlBuilder().with_tag('div').with_class_name('title').add_children_element(
                HtmlBuilder().with_tag('div').add_children_element(
                    HtmlBuilder().with_tag('h' + self.object.titlewrap).add_children_element(self.object.title).build()).build()).build()
            content_element = HtmlBuilder().with_tag('div').with_class_name('content').add_children_element(self.object.contents).build()
            builder.add_children_element(title_element)
            builder.add_children_element(content_element)
        else:
            builder.add_children_element(self.object.contents)
        
        return builder.build().render()