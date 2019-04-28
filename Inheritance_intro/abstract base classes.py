from collections import Container
Container.__abstractmethods__

class OddContainer:
    def __contains__(self, item):
        if isinstance(item, int) and item % 2:
            return True
        return False


class OddLst(OddContainer,list): #contains method will be used from OddContainer here



import abc
class MediaLoader(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def play(self):
        pass

    @abc.abstractproperty
    def ext(self):
        pass

    @classmethod
    def __subclasshook__(cls, C):
        if cls is MediaLoader:
            attrs = set(dir(C))
            if set(cls.__abstractmethods__) <= attrs:
                return True
        return NotImplemented