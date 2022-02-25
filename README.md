# Caching

CacheHelper is a python caching and serialization method that allows to dump/read dictionaries, lists and objects into a file
for caching purposes.

### Installation Notes / Prerequisites
```
pip install -r requirements.txt
```

### Usage
from  cachehelper import CacheHelper
```
a=CacheHelper('appname')
```
CacheHelper class will create a caching directory: example: /Users/user/Library/Caches/appname
```
d={2:3}
a.cache_dump(d,'dictionary_example')
```
cache_dump method will serialize a given object and will save in json format in caching folder with  the given name
 
 /Users/user/Library/Caches/appname/dictionary_example

```
d=a.cache_load('dictionary_example')
```
cache_load method will load json file file into object

