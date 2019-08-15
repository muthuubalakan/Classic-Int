## Classic Int

Int as an int and List.

**Example**
```python
>>> from classic_int import ClassicInt
>>>
>>> c_int = ClassicInt(12345)
>>>
>>> c_int
12345
>>> for number in c_int:
...      print(number)
...
1
2
3
4
5
>>> c_int + 5
12350
>>> c_int - 5
12340
>>> c_int * 2
24690
>>>
>>> c_int.as_list()
[1, 2, 3, 4, 5]
>>>
>>> c_int.index(4)
3
```
