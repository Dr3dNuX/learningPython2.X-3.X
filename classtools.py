
class AttrDisplay:
    
    def getherAttrs(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append('{}={}'.format(key,getattr(self,key)))
        return ', '.join(attrs)
    
    def __repr__(self) -> str:
        return '{}: {}'.format(self.__class__.__name__, self.getherAttrs())
