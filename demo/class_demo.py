from abc import ABCMeta,abstractclassmethod,abstractmethod

# 抽象类
class ABSTestClass(metaclass=ABCMeta):
    """docstring for ABSTestClass"""
    def __init__(self, **kwargs):
        self.public_attr = kwargs['public_attr']
        self._protected_attr = kwargs['protected_attr']
        self.__private_attr = kwargs['private_attr']

    @abstractmethod
    def public_method(self):
        pass


# 普通类
class TestClass(object):
    """docstring for TestClass"""
    def __init__(self, **kwargs):
        self.public_attr = kwargs['public_attr']
        self._protected_attr = kwargs['protected_attr']
        self.__private_attr = kwargs['private_attr']

    @classmethod
    def from_dir(cls, public_attr, protected_attr, private_attr):
        return cls(config=config, public_attr=public_attr, protected_attr=protected_attr, private_attr=private_attr)

    def public_method(self):
        print(self.public_attr)

    def _protected_method(self):
        print(self._protected_attr)

    def __private_method(self):
        print(self.__private_attr)

if __name__=='__main__':
    t = TestClass(public_attr='public', protected_attr='protected', private_attr='private')
    t.public_method()
    t._protected_method()
    # t.__private_method()

