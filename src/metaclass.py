"""
第一步，搞懂__new__ 和 __init__ 的作用
       搞懂super的作用
第二步，理解type可以生成一个新的class
第三步，实现metaclass
"""
print('第一步')


class Fo:
    # 第一步    ： __new__ __init__ 的作用
    # __new__  ： 生成一个实例（一般情况是自动实现，不需要具体实现）
    # __init__ ： 初始化一个实例
    # super(Fo,cls)  ： 1）根据cls生成一个mro的list
    # 详细参考下面代码    2）通过FO定位当前 mro 中的index, 并返回mro[index + 1]
    """
    def super(Fo, cls):
        mro = cls.__class__.mro()
        return mro[mro.index(Fo) + 1]
    """
    def __init__(self, name):
        print('Fo. __init__')
        self.name = name

    def __new__(cls, name):
        print('Fo.__new__')
        print('__new__:', name)
        print(Fo)
        print(cls)
        return super(Fo, cls).__new__(cls)


obj = Fo('FO')

print(obj, 'name ->', obj.name)


print('第二步')
# 第二步，理解type

Foo = type('Foo', (Fo,), {'Name': 'Foo'})
print(Foo, '-->', getattr(Foo, 'Name', 'not exist'))
obj_type = Foo('ggg')
print(obj_type)
print(obj_type.name, getattr(Foo, 'Name', 'not exist'))


print('第三步')


class BaseMetaclass(type):

    def __new__(mcs, name, bases, dct):
        print('BaseMetaclass new')
        dct['pony'] = 'zhiZhi'

        def say(self):
            self.dd = 1
            print('Base say')

        dct['say'] = say

        print(bases)
        print(dct)
        return super(BaseMetaclass, mcs).\
            __new__(mcs, name, bases, dct)


obj_m = BaseMetaclass('myDog', (), {'pony': 'zhuZhiQun'})

print(obj_m, '-->', getattr(obj_m, 'pony', 'pony not exist'))

a = obj_m()
print(a, '-->', getattr(a, 'pony', 'a not exist'))


class MyCls(metaclass=BaseMetaclass):

    def __init__(self):
        print('MyCls init')
        self.clsName = 'MyCls'

    def jump(self):
        print('my cls jump')


print('第四步')
myObj = MyCls()
print(getattr(myObj, 'pony'))
print(isinstance(myObj, BaseMetaclass))
myObj.say()
