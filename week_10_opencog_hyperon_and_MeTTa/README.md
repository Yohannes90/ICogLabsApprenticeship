# Training Week 10: OpenCog Hyperon and MeTTa

## Overview

This repository includes tasks related to **graph rewriting** and basic **list operations** implemented in **MeTTa**. The goal is to explore graph rewriting as a theoretical foundation and apply it in a self-learning context using MeTTa. Additionally, we implement several **list operations** in MeTTa to understand functional programming techniques.

---

## Key Questions

### 1. Graph Rewriting with MeTTa
- What is **graph rewriting** and how does it work?
- What are the different ways to implement **graph rewriting** in MeTTa?
- How can **graph rewriting** be applied for **self-learning**?

### 2. List Operations in MeTTa
Implement five of the following list operations:
- `length`, `is-member`, `append`, `max-value`, `min-value`
- `push`, `pop`, `remove-element`, `remove-duplicate`, `map`
- `filter`, `foldl`, `foldr`, `reverse`, `sort`

---

## Tasks

## **1. Graph Rewriting in MeTTa**

### **Fundamentals of Graph Rewriting**
Graph rewriting transforms a graph structure by applying specific rules through:
- **Pattern Matching**: Identifying subgraphs that fit a predefined structure.
- **Rule Application**: Modifying or replacing matched subgraphs.
- **Iteration**: Continuously applying transformations dynamically.

MeTTa facilitates graph rewriting using the **Space API**, which supports pattern matching, adding, and removing atoms (graph elements).

---

### **Implementing Graph Rewriting in MeTTa**
MeTTa provides multiple mechanisms for graph rewriting:

1. **Pattern Matching with `match`**
   - Finds structures in the graph using unification.
   - Example: Identifying specific links in a graph.

2. **Graph Modification with `add-atom` and `remove-atom`**
   - `add-atom`: Adds new atoms (nodes or edges) dynamically.
   - `remove-atom`: Deletes atoms without reduction.

3. **Combining `match`, `add-atom`, and `remove-atom`**
   - Find a pattern (e.g., circular links).
   - Remove existing edges.
   - Add modified edges to restructure the graph.

   **Example: Reversing Three-Element Loops**
   ```metta
   (link A B)
   (link B C)
   (link C A)
   (link C E)

   ! (match &self (, (link $x $y)
                     (link $y $z)
                     (link $z $x))
               (let () (remove-atom &self (link $x $y))
                       (add-atom &self (link $y $x)) ))
   ```
   - This finds all three-node cycles (`A → B → C → A`) and reverses their direction.
   - The remaining structure (`C → E`) is unchanged.

---

### **Different Strategies for Graph Rewriting**
1. **Direct Pattern Matching with `match`**
   - Matches subgraphs and applies transformations using `remove-atom` and `add-atom`.

2. **Rule-Based Transformations**
   - Stores graph rewriting rules as atoms, which can be dynamically applied.

3. **Learning-Based Rewriting**
   - Uses machine learning models to guide transformations, enabling adaptive systems.

4. **Parallel Rule Execution**
   - Allows multiple transformations to occur simultaneously.
   - Synchronization ensures that graph integrity is maintained.

---

### **Graph Rewriting for Self-Learning**
MeTTa enables **self-learning** AI systems by dynamically modifying knowledge graphs:
- **Adapting its structure** based on new information.
- **Deriving new relationships** by rewriting graph connections.
- **Self-optimizing reasoning** through iterative transformations.

This makes MeTTa powerful for **artificial intelligence, automated reasoning, and adaptive learning systems**. As part of the **OpenCog Hyperon** project, MeTTa provides a robust framework to perform graph rewriting, useful for self-learning and adaptive reasoning.

---


### 2. **List Operations in MeTTa**

The following code provides context on type definitions, helper functions, and basic operations used for the list functions implemented below:

- **List Type Definition**: `List` is defined using `Cons` (for non-empty lists) and `Nil` (for empty lists).
  ```metta
  (: List Type)
  (: Nil List)
  (: Cons (-> Number List List))
  ```

- **Sample List**: A sample list is created using `Cons`, such as:
  ```metta
  (: myList (-> List))
  (= (myList)
    (Cons 42 (Cons 75 (Cons 32 (Cons 23 (Cons 432 (Cons 35 (Cons 94 (Cons 16 (Cons 23 Nil)))))))))
  )
  ```

- **Displaying Lists**: The `show` function recursively prints list values:
  ```metta
    (= (show Nil) ())
    (= (show (Cons $x $xs))
        ($x (show $xs))
    )
  ```

- **Accessing First Element**: The `first_value` function returns the first element in a list:
  ```metta
  (: first_value (-> List Number))
  (= (first_value (Cons $x $xs)) $x)
  ```

- **For Higher-Order Functions**: Examples include `add2` (adds 2 to a number) and `lessThan40` (checks if a number is less than 40).



Here are the list operations implemented in MeTTa:

#### 1. `length`
Calculates the number of elements in a list.

```metta
(: length (-> List Number))
(= (length Nil) 0)
(= (length (Cons $x $xs))
    (+ 1 (length $xs))
)
```

**Example Usage**:
```metta
! (length(myList))  ; [9]
```
---

#### 2. `is_member`
Checks if an element exists in the list.

```metta
(: is_member (-> Number List Bool))
(= (is_member $y Nil) False)
(= (is_member $y (Cons $x $xs))
    (if (== $y $x)
        True
    (is_member $y $xs))
)
```

**Example Usage**:
```metta
! (is_member 432 (myList))  ; [True]
! (is_member 4322 (myList)) ; [False]
```
---

#### 3. `append`
Adds an element to the end of a list.

```metta
(: append (-> Number List List))
(= (append $y Nil) (Cons $y Nil))
(= (append $y (Cons $x $xs))
    (Cons $x (append $y $xs))
)
```

**Example Usage**:
```metta
! (append 332 (myList))  ; [(Cons 42 (Cons 75 (Cons 32 (Cons 23 ...))))]
```
---

#### 6. `push`
Adds an element to the beginning of the list.

```metta
(: push (-> Number List List))
(= (push $x $list) (Cons $x $list))
```

**Example Usage**:
```metta
! (push 43 (myList))  ; [(Cons 43 (Cons 42 (Cons 75 (Cons 32 ...))))]
```
---

#### 7. `pop`
Removes the first element from the list.

```metta
(: pop (-> List List))
(= (pop (Cons $x $xs)) $xs)
```

**Example Usage**:
```metta
! (pop (myList))  ; [(Cons 75 (Cons 32 (Cons 23 ...)))]
```
---

#### 8. `remove-element`
Removes a specific element from the list.

```metta
(: remove_element (-> Number List List))
(= (remove_element $y ()) ())
(= (remove_element $y Nil) Nil)
(= (remove_element $y (Cons $x $xs))
    (if (== $y $x)
        (remove_element $y $xs)
        (Cons $x (remove_element $y $xs))
    )
)
```

**Example Usage**:
```metta
! (remove_element 32 (myList)) ; [(Cons 42 (Cons 75 (Cons 23 (Cons 432 (Cons 35 (Cons 94 (Cons 16 (Cons 23 Nil))))))))]

```
---

#### 10. `map`
Applies a function to each element in the list and returns a new list.

```metta
(: map (-> (-> Number Number) List List))
(= (map $func ()) ())
(= (map $func Nil) Nil)
(= (map $func (Cons $x $xs))
    (Cons ($func $x) (map $func $xs))
)
```

**Example Usage**:
```metta
(map add2 (myList))  ; [(Cons 44 (Cons 77 (Cons 34 (Cons 25 ...))))]
```
---

#### 11. `filter`
Filters the list based on a predicate function.

```metta
(: filter (-> (-> Number Bool) List List))
(= (filter $func ()) ())
(= (filter $func Nil) Nil)
(= (filter $func (Cons $x $xs))
    (if ($func $x)
        (Cons $x (filter $func $xs))
        (filter $func $xs)
    )
)
```

**Example Usage**:
```metta
(filter lessThan40 (myList))  ; [(Cons 32 (Cons 23 (Cons 35 ...)))]
```
---

#### 4. `max_value` (Pending Implementation)

#### 5. `min_value` (Pending Implementation)

#### 9. `remove_duplicate` (Pending Implementation)

#### 12. `foldl` (Pending Implementation)

#### 13. `foldr` (Pending Implementation)

#### 14. `reverse` (Pending Implementation)

#### 15. `sort` (Pending Implementation)

---

### References
- [OpenCog Hyperon Documentation](https://opencog.org/)
- [MeTTa Language Guide](https://github.com/opencog/MeTTa)
- [Given Reference from docs for `Graph rewriting`](https://metta-lang.dev/docs/learn/tutorials/stdlib_overview/working_with_spaces.html#removing-atoms)

---
