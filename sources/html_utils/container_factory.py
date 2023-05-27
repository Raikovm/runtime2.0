from utils import ComponentFactoryBase, HtmlBuilder, HtmlElement

class ContainerFactory(ComponentFactoryBase):
    def __init__(self, VDOM_text): 
        self.object = VDOM_containertext

    def create(self):
        builder = HtmlBuilder()

        if self.securitycode and session["SecurityCode"] and str(session["SecurityCode"]) in self.securitycode.split(";"):
            self.visible = "1"

        id = 'o_' + (self.id).replace('-', '_')

        builder.with_tag('div')
        builder.with_class_name(self.classname)
        builder.add_attribute('id', id)
        self._set_position(builder, self.top, self.left)
        self._set_visibility(builder, self.visible == '0')
        self._set_zindex(builder, self.zindex)

        overflow_settings = {"1": 'hidden', "2": 'scroll', "3": 'visible'}
        builder.add_style('overflow', overflow_settings.get(self.overflow, 'auto'))
        builder.add_style('height', "%spx" % self.height if self.heightauto == "0" else None)
        builder.add_style('background-color', '#%s' % self.backgroundcolor if self.backgroundcolor != "" else None)
        builder.add_style('background-image', "url('%s')" % id2link1(self.backgroundimage) if self.backgroundimage != "" else None)
        repeat_settings = {'1': 'no-repeat', '2': 'repeat-x', '3': 'repeat-y'}
        builder.add_style('background-repeat', repeat_settings.get(self.backgroundrepeat, None))

        builder.add_attribute('footer', 'footer' if self.footer == "1" else None)

        if self.titlewrap != "0":
            title_element = HtmlBuilder().with_tag('div').with_class_name('title').add_children_element(
                HtmlBuilder().with_tag('div').add_children_element(
                    HtmlBuilder().with_tag('h' + self.titlewrap).add_children_element(self.title).build()).build()).build()
            content_element = HtmlBuilder().with_tag('div').with_class_name('content').add_children_element(self.contents).build()
            builder.add_children_element(title_element)
            builder.add_children_element(content_element)
        else:
            builder.add_children_element(self.contents)
        
        return builder.build().render()