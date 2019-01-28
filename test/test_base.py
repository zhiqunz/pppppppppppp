from src.base import FactoryBase


def foo11():
    print('foo11')


def foo22():
    print('foo22')


New_cls11 = FactoryBase.get_new_class(foo11)

obj11 = New_cls11()

obj11.say()
obj11.run()

New_cls22 = FactoryBase.get_new_class(foo22)

obj22 = New_cls22()

obj22.say()
obj22.run()


