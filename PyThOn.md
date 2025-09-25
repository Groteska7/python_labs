# -------------> import json  
### json.loads(<string>) - string = "[1, 2, 4]"
превращает сроку, написанную строго по правилам, в list
```Python
a=json.loads("[1, 2, 3, 4]")
print(a)# ==[1, 2, 3, 4]
```


# -------------> import ast   
### ast.literal_eval(<string>) - string = "[1, 2, 4]"
превращает сроку, написанную по правилам, в list или tuple
```Python
a=json.loads("[1, 2, 3, 4]")
print(a)# == [1, 2, 3, 4]
```
# -------------> import typing 
### TypeVar()
создает тип переменной
```Python
T=TypeVar("T",int,float)
def f(mas: T)
```
### Union
позволяет указать несколько возможных типов для переменной.
```Python
def f(x: Union [int,float]):
```
### Optional
указывает, что переменная может иметь значение определенного типа или быть None.
```Python
def f(x: Optional[int,str]):
```

### Any
представляет неопределенный тип, используется, когда точно неизвестен тип переменной
# -------------> ALL     
### Union
совмещает насколько множеств ( set() )
```Python
result_set.union([1, 2, 3],[1, 5, 6],[2, 6, 1, 4])
print(mas1)# == [1, 2, 3, 5, 6, 4]
```
### Смена названия
```Python
from ast import literal_eval as make_tuple #вызвать iteral_eval из библеотеки ast и переименовать его в make_tuple
```
### tuple
неизменяемые упорядоченные коллекции элементов (кортежи)
