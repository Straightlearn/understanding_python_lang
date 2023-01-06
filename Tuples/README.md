# Python tuple

tuple is a data structure in python, it behavws like a list (data structure) but differ from it.
tuples are immutable while, list are mutable.
tuple is immutable because you can not change its values after intialization.But it values may change if the tuple holds a refrence to any mutable object such as list.
## Note
you may have two tuples contain same values, but they are not pointing at the same memory location.
Example:
```
stanley=(["tall"],"handsome",18)
john=(["tall"],"handsome",18)
  here stanley==john. thats true because
 it contains same values.but, stanley is 
john, will give false because both piints
 at different memory location, and are 
seen as different.
  ```
also note that if you have two  tuples 
that does not contain a list,but has same
 values then they point at the same 
memory location.
Example:
```
obi_score=(88,66,77)
ada_score=(88,66.77)
	these tuples has same values, 
and points at same memory location.
```

