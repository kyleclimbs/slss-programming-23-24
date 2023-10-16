A list in python is a collection of items 
We can store different values in a list
Order matters in a list
# Creating a list
TO make a list we brackets[/] to surround our list 
We separate out the items using

```python 
some_list = ["John", "Tim", "Sara"]
```

# Access Elements in a list
We can grab things from list s using the bracket notation
In our examples above, if I wanted to access "Tim" , I would do the following

```python
some_list[1] # "Tim"
```

## Iterating *n* Number of times

We can iterate/loop for any number pf times.
In Python, we do it in a strange way.

```python
for i in range(<positive integers>)
	<code block>
```

e.g.
```python
# print out "Mr Ubial is pretty cool" 10 times.
for _ in range(20):
	print()
```

## range() function
 Range is a function that gives a sequence of numbers starting at zero by default. By default it also goes up by one. It stops before the number that you provide as an input.

```python
range(100) -> Sequence(0,...,100)
```
We can modify range() to start, stop, and count up/down by different numbers.
eg.
```python
range(0, 100)  #Sequence(o,1,...,99)
range(-10, 10) #Sequence(-10,-9, ..., 9)
range(0, 100, 2) #Sequence(0, 2, 4, ..., 98)
range(100, 0 , -1) #Sequence(100, 99, ..., 1)
```

## break
Break allows us to stop the looping. Once break is reached, no other code underneath it in the for loop will run.