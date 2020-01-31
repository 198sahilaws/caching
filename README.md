# Caching

CacheHelper is a python caching and serialization method that allows to dump/read dictionaries, lists and objects into a file
for caching purposes.

### Installation Notes / Prerequisites
   pip install appdirs
   pip install pickle

### Usage
from  cachehelper import CacheHelper
```
a=CacheHelper('appname')
```
CacheHelper class will create a caching directory: example: /Users/user/Library/Caches/appname
```
d={2:3}
a.pickle_dump(d,'dictionary_example')
```
pickle_dump method will serialize a given object and will save in caching folder with given name
 
 /Users/user/Library/Caches/appname/dictionary_example

```
d=a.pickle_load('dictionary_example')
```
pickle_load method will load binary serialized file into object


