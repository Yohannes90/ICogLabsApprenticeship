# Training Week 6: Functional Programming with Haskell Assignment

## Overview

This repository contains a series of Haskell tasks that demonstrate key functional programming concepts including `map`, `filter`, `foldl`, `foldr`, `sum`, `product`, `count`, function composition(`.`), and counting the occurrences of specific elements in a list(`countOccerence`).

## Resources

- [Learn You a Haskell - Chapters 2, 4, and 5](https://learnyouahaskell.github.io/chapters.html)
- [YouTube Video - Haskell Functional Programming](https://www.youtube.com/watch?v=02_H3LjqMr8)

## Tasks

### 1. `map`

`map'` applies a given function to each element in a list and returns a new list.

```haskell
map' :: (a -> b) -> [a] -> [b]
map' func xs = [func x | x <- xs]
```

**Example Usage:**

```haskell
map' (*2) [1, 2, 3]   -- [2, 4, 6]
```

---

### 2. `filter`

`filter'` filters the elements of a list based on a predicate function.

```haskell
filter' :: (a -> Bool) -> [a] -> [a]
filter' func xs = [x | x <- xs, func x]
```

**Example Usage:**

```haskell
filter' even [1, 2, 3, 4]   -- [2, 4]
```

---

### 3. `foldl` (Fold Left)

`foldl'` processes a list from the left, applying a function and accumulating a result.

```haskell
foldl' :: (b -> a -> b) -> b -> [a] -> b
foldl' _ z [] = z
foldl' func z (x:xs) = foldl' func (func z x) xs
```

**Example Usage:**

```haskell
foldl' (+) 0 [1, 2, 3]      -- 6
```

---

### 4. `foldr` (Fold Right)

`foldr'` processes a list from the right, applying a function and accumulating a result.

```haskell
foldr' :: (a -> b -> b) -> b -> [a] -> b
foldr' _ z [] = z
foldr' func z (x:xs) = func x (foldr' func z xs)
```

**Example Usage:**

```haskell
foldr' (+) 0 [1, 2, 3]      -- 6
```

---

### 5. `sum`

`sum'` computes the sum of a list of numbers.

```haskell
sum' :: Num a => [a] -> a
sum' [] = 0
sum' (x:xs) = x + sum' xs
```

**Example Usage:**

```haskell
sum' [1, 2, 3]              -- 6
```

---

### 6. `product`

`product'` computes the product of a list of numbers.

```haskell
product' :: Num a => [a] -> a
product' [] = 1
product' (x:xs) = x * product' xs
```

**Example Usage:**

```haskell
product' [1, 2, 3]          -- 6
```

---

### 7. `count`

`count'` counts the number of elements in a list.

```haskell
count' :: [a] -> Int
count' [] = 0
count' (_:xs) = 1 + count' xs
```

**Example Usage:**

```haskell
count' [1, 2, 3]            -- 3
```

Alternatively, you can use `length'` to achieve the same result:

```haskell
length' :: [a] -> Int
length' [] = 0
length' xs = sum' [1 | _ <- xs]
```

**Example Usage:**

```haskell
length' [1, 2, 3]           -- 3
```

---

#### 7.2. Count Occurrence of a Given Integer

`countOccerence` counts how many times a given integer appears in a list.

```haskell
countOccerence :: [Int] -> Int -> Int
countOccerence [] _ = 0
countOccerence xs z = sum' [1 | x <- xs, x == z]
```

**Example Usage:**

```haskell
countOccerence [2, 2, 2, 3, 4] 2   -- 3
```

---

### 8. `compose` (Function Composition)

In Haskell, function composition allows you to combine two functions into one using the `(.)` operator.

```haskell
compose' :: (b -> c) -> (a -> b) -> (a -> c)
compose' f g = \x -> f (g x)
```

**Example Usage:**

```haskell
compose' not even 3         -- True
```

### Additional Examples of Composition:

```haskell
double :: Int -> Int
double x = x * 2

increment :: Int -> Int
increment x = x + 1

compose' double increment 10     -- 22
compose' increment double 10     -- 21
```

---

## Conclusion

These tasks demonstrate the core principles of functional programming in Haskell, including higher-order functions, recursion, and function composition.
