# serialization
python caching and serialization


### Installation Notes / Prerequisites
   pip install appdirs
   pip install pickle

### Usage
from  serialization import Serialization
> a=Serialization('appname')

'Serialization class will create a caching directory: example: /Users/user/Library/Caches/appname'

d={2:3}
a.pickle_dump(d,'dictionary_example')

'pickle_dump' method will serialize a given object and will save in caching folder with given name'
'/Users/user/Library/Caches/appname/dictionary_example'


d=a.pickle_load('dictionary_example')

'pickle_load' method will sload binary serialized file into object


