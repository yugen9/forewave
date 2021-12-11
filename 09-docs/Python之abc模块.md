# Python之abc模块

> abc：Abstract Base Classes
>
> 作用：在代码中定义和使用抽象基类进行API检查。

### 1. 为什么使用abc？

> Abstract base classes由一组接口组成，检查比`hasattr()`更严格。通过定义一个抽象基类，可以为一组子类定义一个通用的API。这对于第三方为应用提供插件等非常有用，另外当您在一个大型的团队中工作或在一个大型的代码库中，同时将所有的类放在您的头脑中是困难或不可能的时，它也可以帮助您。

### 2. abc怎么工作

*abc通过把基类中的方法标记为抽象方法，并且注册具体类为基类的实现的方式工作。*

定义基类: abc_base.py

```python
import abc

class PluginBase(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def load(self, input):
        """Retrieve data from the input source and return an object."""
        return

    @abc.abstractmethod
    def save(self, output, data):
        """Save the data object to the output."""
        return1234567891011121314
```

**有两种方法表明一个具体类实现了一个抽象类**

**a) 第一种方法：通过使用abc注册，这种方法下`RegisteredImplementation`并不是由`PluginBase`派生，而是通过注册方式.**

abc_register.py

```python
import abc
from abc_base import PluginBase

class RegisteredImplementation(object):

    def load(self, input):
        return input.read()

    def save(self, output, data):
        return output.write(data)

PluginBase.register(RegisteredImplementation)

if __name__ == '__main__':
    print 'Subclass:', issubclass(RegisteredImplementation, PluginBase)
    print 'Instance:', isinstance(RegisteredImplementation(), PluginBase)12345678910111213141516
```

*output:*

```bash
Subclass: True
Instance: True12
```

**b) 第一种方法：通过实现`PluginBase`API，是派生.**

abc_subclass.py

```python
import abc
from abc_base import PluginBase

class SubclassImplementation(PluginBase):

    def load(self, input):
        return input.read()

    def save(self, output, data):
        return output.write(data)

if __name__ == '__main__':
    print 'Subclass:', issubclass(SubclassImplementation, PluginBase)
    print 'Instance:', isinstance(SubclassImplementation(), PluginBase)1234567891011121314
```

*output:*

```bash
Subclass: True
Instance: True12
```

**两种方式的不同：**

1. `SubclassImplementation`在`PluginBase.__subclasses__()`中，而`RegisteredImplementation`不在.
2. `SubclassImplementation`必须实现`PluginBase`中的所有抽象方法，否则会在运行时报错；而`RegisteredImplement`不需要.

### 3. 抽象方法的实现

**在抽象类中抽象方法也可以提供通用的逻辑实现，这样具体类中就可以通过调用`super()`重用抽象方法的实现.**

```python
import abc
from cStringIO import StringIO

class ABCWithConcreteImplementation(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def retrieve_values(self, input):
        print 'base class reading data'
        return input.read()

class ConcreteOverride(ABCWithConcreteImplementation):

    def retrieve_values(self, input):
        base_data = super(ConcreteOverride, self).retrieve_values(input)
        print 'subclass sorting data'
        response = sorted(base_data.splitlines())
        return response

input = StringIO("""line one
line two
line three
""")

reader = ConcreteOverride()
print reader.retrieve_values(input)
print123456789101112131415161718192021222324252627
```

*output:*

```bash
base class reading data
subclass sorting data
['line one', 'line three', 'line two']123
```

### 4. 抽象特性(Abstract Properties)

*如果你的API规范中还包括属性，那么你可以使用`@abstractproperty`来定义.*

```python
import abc

class Base(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractproperty
    def value(self):
        return 'Should never get here'


class Implementation(Base):

    @property
    def value(self):
        return 'concrete property'


try:
    b = Base()
    print 'Base.value:', b.value
except Exception, err:
    print 'ERROR:', str(err)

i = Implementation()
print 'Implementation.value:', i.value12345678910111213141516171819202122232425
```

*因为`Base`只有property `value`getter方法的抽象版本，所有它不能被实例化.*

*output:*

```bash
ERROR: Can't instantiate abstract class Base with abstract methods value
Implementation.value: concrete property12
```

**定义抽象的读写特性**

```python
import abc

class Base(object):
    __metaclass__ = abc.ABCMeta

    def value_getter(self):
        return 'Should never see this'

    def value_setter(self, newvalue):
        return

    value = abc.abstractproperty(value_getter, value_setter)


class PartialImplementation(Base):

    @abc.abstractproperty
    def value(self):
        return 'Read-only'


class Implementation(Base):

    _value = 'Default value'

    def value_getter(self):
        return self._value

    def value_setter(self, newvalue):
        self._value = newvalue
    #定义具体类的property时必须与抽象类的abstract property相同。如果只覆盖其中一个将不会工作。
    value = property(value_getter, value_setter)


try:
    b = Base()
    print 'Base.value:', b.value
except Exception, err:
    print 'ERROR:', str(err)

try:
    p = PartialImplementation()
    print 'PartialImplementation.value:', p.value
except Exception, err:
    print 'ERROR:', str(err)

i = Implementation()
print 'Implementation.value:', i.value

i.value = 'New value'
print 'Changed value:', i.value123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051
```

*output:*

```bas
ERROR: Can't instantiate abstract class Base with abstract methods value
ERROR: Can't instantiate abstract class PartialImplementation with abstract methods value
Implementation.value: Default value
Changed value: New value1234
```

**使用装饰器来实现读写的抽象特性，读和写的方法名应该相同**

```python
import abc

class Base(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractproperty
    def value(self):
        return 'Should never see this'

    @value.setter
    def value(self, newvalue):
        return


class Implementation(Base):

    _value = 'Default value'

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, newvalue):
        self._value = newvalue


i = Implementation()
print 'Implementation.value:', i.value

i.value = 'New value'
print 'Changed value:', i.value1234567891011121314151617181920212223242526272829303132
```

*output:*

```bash
Implementation.value: Default value
Changed value: New value
```