class ComponentFactoryBase(object):
    def create(self):
        raise NotImplementedError("Derived classes must implement create() method.")


    def _set_position(self, builder, top, left):
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
                "\"%s\"" % family or "",                
                "bold" if is_bold else "",
                "italic" if is_italic else ""]
        builder.add_style.add_style("font", " ".join(font))



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
        attributes = " ".join("'{}'=\"{}\"".format(k, v) for k, v in self.html_attributes.items())
        css_merge_script = ("const styleFromCss = '{0}'"
                            "styles = jss.default.merge(styleFromCss, styles)").format(self.css) if self.css is not None else ""
        jss_script = ("<script>"
                      "(function() {{"
                      "let styles = {{{0} : {1}}};"
                      "{2}" 
                      "const sheet = jss.default.createStyleSheet(styles);"
                      "sheet.attach();"
                      "}})();"
                      "</script>").format(self.class_name, jss, css_merge_script)
        return "<{0} class=\"{1}\" {2}>{3}{4}</{0}>".format(self.tag, class_name, attributes, jss_script, children)


    def __str__(self):
        return self.render()


class HtmlBuilder(object):
    def __init__(self):
        self._element = HtmlElement(None, {}, None, [], None)


    def add_style(self, style, value):
        if value is not None:
            self._element.jss[style] = value
        elif style in jss: 
            del jss[style]
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

    def add_attribute(self, attribute, value)
        if value is not None:
            self._element.html_attributes[style] = value
        elif style in html_attributes: 
            del html_attributes[style]
        return self


    def build(self):
        return self._element

def main():

    child_builder = HtmlBuilder()
    child_element = (child_builder.add_style('color', 'blue')
                   .with_tag('p')
                   .add_children_element("LOL")
                   .build())
    builder = HtmlBuilder()
    html_element = (builder.add_style('color', 'red')
                   .add_style('fontSize', '20px')
                   .with_tag('div')
                   .add_children_element('This is the parent element')
                   .add_children_element(child_element)
                   .build())
    print(html_element)
