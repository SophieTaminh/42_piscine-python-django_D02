import elem
 
class Html(elem.Elem):
    def __init__(self, elem=None, tag='html', attr={}, tag_type='double'):
        super().__init__(content=elem, tag=tag, attr=attr)

class Head(elem.Elem):
    def __init__(self, elem=None, tag='head', attr={}, tag_type='double'):
        super().__init__(content=elem, tag=tag, attr=attr)

class Body(elem.Elem):
    def __init__(self, elem=None, tag='body', attr={}, tag_type='double'):
        super().__init__(content=elem, tag=tag, attr=attr)

class title(elem.Elem):
    def __init__(self, elem=None, tag='title', attr={}, tag_type='double'):
        super().__init__(content=elem, tag=tag, attr=attr)

class meta(elem.Elem):
    def __init__(self, elem=None, tag='meta', attr={}, tag_type='simple'):
        super().__init__(content=elem, tag=tag, attr=attr)

class img(elem.Elem):
    def __init__(self, elem=None, tag='img', attr={}, tag_type='simple'):
        super().__init__(content=elem, tag=tag, attr=attr)

class table(elem.Elem):
    def __init__(self, elem=None, tag='table', attr={}, tag_type='double'):
        super().__init__(content=elem, tag=tag, attr=attr)

class th(elem.Elem):
    def __init__(self, elem=None, tag='th', attr={}, tag_type='double'):
        super().__init__(content=elem, tag=tag, attr=attr)

class tr(elem.Elem):
    def __init__(self, elem=None, tag='tr', attr={}, tag_type='double'):
        super().__init__(content=elem, tag=tag, attr=attr)

class td(elem.Elem):
    def __init__(self, elem=None, tag='td', attr={}, tag_type='double'):
        super().__init__(content=elem, tag=tag, attr=attr)

class ul(elem.Elem):
    def __init__(self, elem=None, tag='ul', attr={}, tag_type='double'):
        super().__init__(content=elem, tag=tag, attr=attr)

class ol(elem.Elem):
    def __init__(self, elem=None, tag='ol', attr={}, tag_type='double'):
        super().__init__(content=elem, tag=tag, attr=attr)

class li(elem.Elem):
    def __init__(self, elem=None, tag='li', attr={}, tag_type='double'):
        super().__init__(content=elem, tag=tag, attr=attr)

class h1(elem.Elem):
    def __init__(self, elem=None, tag='h1', attr={}, tag_type='double'):
        super().__init__(content=elem, tag=tag, attr=attr)

class h2(elem.Elem):
    def __init__(self, elem=None, tag='h2', attr={}, tag_type='double'):
        super().__init__(content=elem, tag=tag, attr=attr)

class p(elem.Elem):
    def __init__(self, elem=None, tag='p', attr={}, tag_type='double'):
        super().__init__(content=elem, tag=tag, attr=attr)

class div(elem.Elem):
    def __init__(self, elem=None, tag='div', attr={}, tag_type='double'):
        super().__init__(content=elem, tag=tag, attr=attr)

class span(elem.Elem):
    def __init__(self, elem=None, tag='span', attr={}, tag_type='double'):
        super().__init__(content=elem, tag=tag, attr=attr)

class hr(elem.Elem):
    def __init__(self, elem=None, tag='hr', attr={}, tag_type='simple'):
        super().__init__(content=elem, tag=tag, attr=attr)

class br(elem.Elem):
    def __init__(self, elem=None, tag='br', attr={}, tag_type='simple'):
        super().__init__(content=elem, tag=tag, attr=attr)

#------------------------------------------------------------
if __name__ == '__main__':
    #instance_html =  html()
    print( Html( [Head(title(elem = elem.Text('"Hello ground!"'))), Body([h1(elem = elem.Text('"Oh no, not again!"')),img(attr={'src' : '"http://i.imgur.com/pfp3T.jpg"'})])] ) )
   