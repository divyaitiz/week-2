
# Interview Answers — Part C

## Q2 — Duplicate Detection

### Problem

Write a function:

```

find_duplicates(lst)

````

Return a **set of elements that appear more than once**.

Constraints:

- Use **set operations only**
- No `Counter`
- No nested loops
- Target complexity **O(n)**

---

### Solution

```python
def find_duplicates(lst):

    seen = set()
    duplicates = set()

    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)

    return duplicates
````

---

### Example

```python
print(find_duplicates([1,2,3,2,4,1,5]))
```

Output

```
{1, 2}
```

---

### Explanation

The algorithm maintains two sets:

* **seen** → stores elements encountered for the first time
* **duplicates** → stores elements that appear more than once

Process:

1. Iterate through the list once.
2. If an element already exists in `seen`, add it to `duplicates`.
3. Otherwise add it to `seen`.

This ensures every element is processed once.

---

### Complexity

```
Time Complexity: O(n)
Space Complexity: O(n)
```

Set lookups (`in`) operate in constant time on average.

---

# Q3 — Debug Problem

## Given Code

```python
def unique_to_each(a, b):
    result = set(a) - set(b)
    return list(result)
```

Test:

```python
unique_to_each([1,2,3], [3,4,5])
```

Expected output:

```
[1,2,4,5]
```

Actual output:

```
[1,2]
```

---

## Why This Happens

The expression:

```
set(a) - set(b)
```

computes **set difference**.

Meaning:

```
elements in set(a) but not in set(b)
```

For the test case:

```
set(a) = {1,2,3}
set(b) = {3,4,5}
```

So:

```
set(a) - set(b) = {1,2}
```

This returns elements **unique to list `a` only**, not elements unique to both lists.

---

## Correct Approach

To return elements that appear in **either list but not both**, we use **symmetric difference**.

Mathematically:

```
(A - B) ∪ (B - A)
```

Python provides an operator for this:

```
^
```

---

## Fixed Function

```python
def unique_to_each(a, b):

    result = set(a) ^ set(b)

    return list(result)
```

---

### Example

```python
print(unique_to_each([1,2,3], [3,4,5]))
```

Output:

```
[1,2,4,5]
```

---

## Key Interview Insight

Understanding the difference between set operations is important:

| Operation | Meaning                     |
| --------- | --------------------------- |
| `A - B`   | Elements only in A          |
| `A ∩ B`   | Elements common to both     |
| `A ∪ B`   | All elements                |
| `A ^ B`   | Elements unique to each set |

For this problem, the correct operation is **symmetric difference (`^`)**.

```
```
