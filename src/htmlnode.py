class HTMLNode():
    def __init__(self,tag=None,value=None,children=None,props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    def to_html(self):
        raise NotImpementedError
    def props_to_html(self):
        if self.props is None:
            return ""
        return ' '+' '.join(list(map(lambda prop: f'{prop[0]}="{prop[1]}"',self.props.items())))

    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props}"

class LeafNode(HTMLNode):
    def __init__(self, tag,value,props=None):
        super().__init__(tag, value,None, props)
    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}>{self.value}</{self.tag}>"

        
    def __repr__(self):
        return f"LeafNode(tag={self.tag}, value={self.value}, props={self.props}"


class ParentNode(HTMLNode):
    def __init__(self,tag,children,props=None):
        super().__init__(tag,None,children,props)

    def __repr__(self):
        return f"ParentNode(tag={self.tag}, children={self.children}, props={self.props}"

    def to_html(self):
        if self.tag is None:
            raise ValueError("All parent nodes must have tags")
        if self.children is None:
            raise ValueError("All parent nodes must have children")
        children_html = ""
        for item in self.children:
            children_html+= item.to_html()
        return f"<{self.tag}>{children_html}</{self.tag}>"

