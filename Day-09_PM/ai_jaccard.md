
# AI-Augmented Task — Jaccard Similarity

## 1. Prompt Used

```

Write a Python function that calculates the Jaccard similarity between two sets of strings. Explain what Jaccard similarity is and where it is used in industry.

````

---

# 2. AI Generated Code

Example AI-generated implementation:

```python
def jaccard_similarity(set_a, set_b):

    intersection = set_a.intersection(set_b)
    union = set_a.union(set_b)

    return len(intersection) / len(union)
````

---

# 3. What is Jaccard Similarity?

Jaccard similarity is a metric used to measure the similarity between two sets.

The formula is:

```
J(A,B) = |A ∩ B| / |A ∪ B|
```

Where:

* **A ∩ B** represents the intersection (common elements)
* **A ∪ B** represents the union (all unique elements)

The result ranges from:

```
0 → no similarity
1 → identical sets
```

---

# 4. Testing the Code

Test data:

```python
set_a = {'python','java','sql'}
set_b = {'python','sql','docker','aws'}

print(jaccard_similarity(set_a, set_b))
```

### Calculation

Intersection:

```
{'python','sql'} → size = 2
```

Union:

```
{'python','java','sql','docker','aws'} → size = 5
```

Result:

```
2 / 5 = 0.4
```

Output:

```
0.4
```

The formula implemented in the AI-generated code is **correct**.

---

# 5. Edge Case Analysis

The AI-generated function does **not handle empty sets**.

Example:

```
jaccard_similarity(set(), set())
```

This produces:

```
ZeroDivisionError
```

because the union size becomes zero.

---

# 6. Improved Version

```python
def jaccard_similarity(set_a, set_b):

    union = set_a | set_b

    if len(union) == 0:
        return 0

    intersection = set_a & set_b

    return len(intersection) / len(union)
```

This prevents division-by-zero errors when both sets are empty.

---

# 7. Industry Applications

Jaccard similarity is widely used in data science and machine learning systems.

In **recommendation systems**, it measures similarity between users or products based on shared preferences or features.
In **natural language processing**, it helps compare documents or keyword sets to determine text similarity.
In **plagiarism detection**, it identifies overlapping words or phrases between documents to detect copied content.
It is also used in **search engines and data deduplication systems** to detect similar or duplicate records in large datasets.

---

# Key Takeaway

Jaccard similarity is a simple but powerful metric for comparing sets. It is commonly used in recommendation engines, document comparison, and large-scale data analysis systems where measuring similarity between collections of items is important.

```
```
