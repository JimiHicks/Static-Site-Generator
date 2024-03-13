class HTMLNODE:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("to_html method not implemtented")
    
    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html
 

    def __repr__(self):
        return f"HTMLCODE({self.tag}, {self.value}, {self.children}, {self.props})"
    
class LeafNode(HTMLNODE):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.value:
            raise ValueError("Leafnode requires a value")
        elif self.tag == None:
            return f"{self.value}"
        html_props = self.props_to_html()
        if html_props:
            return f"<{self.tag} {html_props}>{self.value}</{self.tag}>" 
        elif not html_props:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    
class ParentNode(HTMLNODE):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("Tag not provided")
        if not self.children:
            raise ValueError("Has no children")
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
        
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
    

   