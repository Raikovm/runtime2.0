class ComponentFactoryBase(object):
    def create(self):
        raise NotImplementedError("Derived classes must implement create() method.")

    def _set_position(self, builder, top, left):
        builder.add_style("position", "absolute")
        builder.add_style("top", "%spx" % top)
        builder.add_style("left", "%spx" % left)


    def _set_visibility(self, builder, visibility):
        if not visibility: 
            builder.add_style("display", "none")
        else: 
            builder.add_style("display", "initial")


    def _set_zindex(self, builder, index):
        builder.add_style("z-index", index)


    def _set_size(self, builder, width, height):
        builder.add_style("width", "%spx" % width)
        builder.add_style("height", "%spx" % height)


    def _set_font(self, builder, size, family, is_bold, is_italic):
        font = [
                "%spx" % size or "12px",
                "%s" % family or "",                
                "bold" if is_bold else "",
                "italic" if is_italic else ""]
        builder.add_style("font", " ".join(font))

class TextFactory(ComponentFactoryBase):
    def __init__(self, VDOM_text): 
        self.object = VDOM_text

    def create(self):
        builder = HtmlBuilder()

        self._set_position(builder, self.object.top, self.object.left)
        self._set_visibility(builder, self.object.visible == '0')
        self._set_zindex(builder, self.object.zindex)
        self._set_size(builder, self.object.width, self.object.height)
        self._set_font(builder, self.object.fontsize, self.object.fontfamily, self.object.fontweight == 'bold', self.object.fontstyle == 'italic')
        
        builder.with_tag(self.object.htmltag)
        builder.add_css('%s' % self.object.css if self.object.css else None)

        builder.add_style('overflow', 'auto')
        builder.add_style('text-align', self.object.align)
        builder.add_style('color', '#%s' % self.object.color if self.object.color else None)
        builder.add_style('text-decoration', self.object.textdecoration)
        builder.with_class_name(self.object.classname)
        builder.add_attribute("title", self.object.hint.replace('"', '&quot;'))
        builder.add_attribute("id", self.object.id_special)
        builder.add_attribute("debug_info", self.object.debug_info)

        builder.add_children_element(self.object.value)

        return builder.build().render()

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

class HtmlElement(object):
    def __init__(self, tag, jss, css, children, class_name, html_attributes):
        self.tag = tag
        self.jss = jss
        self.css = css
        self.children = children
        self.class_name = class_name
        self.html_attributes = html_attributes

    def render(self):
        jss = ", ".join("'{}': '{}'".format(k, v) for k, v in self.jss.items())
        children = "".join(str(child) for child in self.children)
        class_name = self.class_name if self.class_name is not None else self.tag
        attributes = " ".join("{}=\"{}\"".format(k, v) for k, v in self.html_attributes.items())
        css_merge_script = ("const styleFromCss = '{0}'"
                            "styles = jss.default.merge(styleFromCss, styles)").format(self.css) if self.css is not None else ""
        jss_script = ("<script>"
                      "{{"
                      "let styles = {{{0} : {{{1}}}}};"
                      "{2}" 
                      "let sheet = jss.default.createStyleSheet(styles).attach();"
                      "let element = document.currentScript.parentElement;"
                      "element.classList.add(sheet.classes.{0});"
                      "}};"
                      "</script>").format(self.class_name, jss, css_merge_script)
        return "<{0} class=\"{1}\" {2}>{3}{4}</{0}>".format(self.tag, class_name, attributes, jss_script, children)


    def __str__(self):
        return self.render()

class HtmlBuilder(object):
    def __init__(self):
        self._element = HtmlElement(None, {}, None, [], None, {})


    def add_style(self, style, value):
        if value is not None:
            self._element.jss[style] = value
        return self


    def with_tag(self, tag_name):
        self._element.tag = tag_name
        return self


    def add_children_element(self, child_element):
        self._element.children.append(child_element)
        return self


    def with_class_name(self, class_name):
        self._element.class_name = class_name
        return self


    def add_css(self, text):
        self._element.css = text
        return self

    def add_attribute(self, attribute, value):
        if value is not None:
            self._element.html_attributes[attribute] = value 
        elif attribute in self._element.html_attributes: 
            del self._element.html_attributes[attribute] 
        return self


    def build(self):
        return self._element

class VDOM_text:
    def __init__(self):
        self.top = 10
        self.left = 10
        self.visible = '0'
        self.zindex = 1
        self.width = 100
        self.height = 100
        self.fontsize = 16
        self.fontfamily = 'Arial'
        self.fontweight = 'bold'
        self.fontstyle = 'italic'
        self.htmltag = 'p'
        self.css = None
        self.color = '000000'
        self.textdecoration = 'underline'
        self.classname = 'mytext'
        self.hint = 'This is a hint'
        self.id_special = 'text-id'
        self.debug_info = 'debug info'
        self.align = 'center'
        self.value = 'TEXT'

class VDOM_richtext:
    def __init__(self):
        self.id = 'id'
        self.classname = 'richtext'
        self.top = 10
        self.left = 10
        self.zindex = 1
        self.width = 100
        self.height = 50
        self.overflow = '2'
        self.align = 'left'
        self.color = '000000'
        self.font = 'Arial'
        self.underlined = '1'
        self.strikethrough = '1'
        self.visible = '0'
        self.value = 'This is a rich text'

class VDOM_container:
    def __init__(self):
        self.id = 'id-1'
        self.classname = 'container'
        self.top = 200
        self.left = 10
        self.visible = '0'
        self.zindex = 1
        self.overflow = '1'
        self.height = 100
        self.heightauto = '1'
        self.backgroundcolor = 'FFFFFF'
        self.backgroundimage = ''
        self.backgroundrepeat = '1'
        self.footer = '0'
        self.titlewrap = '1'
        self.title = 'Container Title'
        self.contents = '<p>Container contents</p>'
        self.securitycode = None

class VDOM_hypertext:
    def __init__(self):
        self.id = 'id-1'
        self.classname = 'hypertext'
        self.top = 10
        self.left = 300
        self.visible = '0'
        self.zindex = 1
        self.width = 100
        self.height = 50
        self.nostyle = '0'
        self.overflow = '1'
        self.htmlcode = '<a href="#">This is an html code</a>'

class VDOM_formbutton:
    def __init__(self):
        self.id = 'button1'
        self.classname = 'form'
        self.type = 0  
        self.tabindex = 1
        self.label = 'Submit'
        self.name = 'submitbutton'
        self.visible = '0'
        self.top = 10
        self.left = 410
        self.zindex = 1
        self.width = 100
        self.height = 30
        self.fontsize = '12'
        self.fontfamily = 'Arial'
        self.fontweight = 'normal'
        self.fontstyle = 'normal'


def main():
    print("-------RichText html:")
    vdom_richtext = VDOM_richtext()
    rich_text_factory = RichTextFactory(vdom_richtext)
    print(rich_text_factory.create())
    vdom_text = VDOM_text()
    text_factory = TextFactory(vdom_text)
    print("-------Text html:")
    print(text_factory.create())
    vdom_container = VDOM_container()
    container_factory = ContainerFactory(vdom_container)
    print("-------Container html:")
    print(container_factory.create())
    vdom_hypertext = VDOM_hypertext()
    print("-------Hypertext html:")
    hyper_text_factory = HyperTextFactory(vdom_hypertext)
    print(hyper_text_factory.create())
    vdom_formbutton = VDOM_formbutton()
    form_button_factory = FormButtonFactory(vdom_formbutton)
    print("-------FormButton html:")
    print(form_button_factory.create())


if __name__ == "__main__":
    main()


