-- Exercises
-- create a function that takes two numbers and returns their product minus 10
productMinus10 :: Int -> Int -> Int
productMinus10 x y = x * y - 10


-- create list compershension that creates a list of odd numbers from 0 to 50
oddFrom0to50 = [x | x <- [1..50], x `mod` 2 /= 0]


-- a function that filters numbers greate than 100 from a given list
-- approch 1
filter100above :: [Int] -> [Int]
filter100above list = filter (> 100) list
-- approch 2
filter100above2 :: [Int] -> [Int]
filter100above2 list = [x | x <- list, x > 100]


-- write a function that calculates the sum of squares for all even numbers in a list
-- approch 1
sumSquareForEven :: [Int] -> Int
sumSquareForEven list = sum [x * x | x <- list, x `mod` 2 == 0]
-- same approch but was confused by the 'xs' use form the given solution
sumSquareForEven2 :: [Int] -> Int
sumSquareForEven2 xs = sum [x^2 | x <- xs, x `mod` 2 == 0]


-- function that takes two lists and returns a list of their pairwise products
-- approch 1 (Error)
-- pairwiseProduct :: [Int] -> [Int] -> [Int]
-- pairwiseProduct list list2 = [x * y | x <- list, y <- list2]
-- approch 2
pairwiseProduct :: [Int] -> [Int] -> [Int]
-- pairwiseProduct list list2 = [x * y | (x, y) <- zip list list2]
pairwiseProduct xs ys = [x * y | (x, y) <- zip xs ys]


-- function to implement builtin map function
-- approch 1
myMap :: (a -> b) -> [a] -> [b]
myMap func a = [func x| x <- a]
-- approch 2
myMap2 :: (a -> b) -> [a] -> [b]
myMap2 func (x:xs) = func x : myMap2 func xs


-- below this needs revison to understand and be able to reimplement them
----------------------------------------

-- check a if a list is sorted in ascending order
-- approch 1
checkSortAsc :: [Int] -> Bool
checkSortAsc [] = True
checkSortAsc [_] = True
checkSortAsc xs = sort xs == xs
-- approch 2
checkSortAsc2 :: [Int] -> Bool
checkSortAsc2 [] = True
checkSortAsc2 [_] = True
checkSortAsc2 (x:y:xs) = x <= y && checkSortAsc2 (y:xs)


-- a list comperhension to generate the first 20 fibonacci numbers
fibonacci20 :: [Int]
fibonacci20 = take 20 $ map fst $ iterate (\(a, b) -> (b, a + b)) (0, 1)


-- a function that removes duplicates from a list using list comperhension
-- removeDuplicate :: [Int] -> [Int]
-- removeDuplicate xs = [x | x <- xs, y <- xs, y /= x]
-- answer
removeDuplicates :: Eq a => [a] -> [a]
removeDuplicates xs = [x | (x, idx) <- zip xs [0..], x `notElem` take idx xs]

-- revision till here
--------------------------------------------------------------


-- Higher-Order Functions
-- 1. Mapping Squares: a function that takes in a list of integers and return them squared
square' :: Int -> Int
square' a = a^2
-- square' a = a * a

map' :: (Int -> Int) -> [Int] -> [Int]
map' func xs = [func x| x <- xs]

squareList :: [Int] -> [Int]
squareList xs = map' square' xs


-- 2. Filtering Even Numbers: a function that filters out even numbers
even' :: Int -> Bool
even' x = x `mod` 2 == 0

filter' :: [Int] -> [Int]
filter' xs = [x | x <- xs, even x]


-- 3. Sum of Squares: a function that calculates sum of functions
sum' :: [Int] -> Int
sum' [] = 0
sum' (x:xs) = x + sum' xs


-- 4. Custom Fold: a custom fold left function implementation
-- foldl' :: (b -> a -> b) -> b -> [a] -> b


-- Recursion
-- 5. Factorial: a recursive function to calculate factorial
product' :: [Int] -> Int
product' [] = 1
product' (x:xs) = x * product' xs

factorial' :: Int -> Int
factorial' x = product' [1..x]


-- 6. Fibonacci Sequence: a recursive function to generate fibonacci series
fibonacci :: Int -> Int
fibonacci 0 = 0
fibonacci 1 = 1
fibonacci n = fibonacci (n - 1) + fibonacci (n - 2)


-- 7. List Length: a function to find the length of a list
-- approch 1
length' :: [Int] -> Int
length' [] = 0
length' xs = sum' [1 | _ <- xs]
-- appproch 2
count' :: [Int] -> Int
count' [] = 0
count' (x:xs) = 1 + count' xs

-- Pattern Matching
-- 8. Safe Head: a function that returns the first element of a given element, else none if it doesn'r exist
safeHead :: [a] -> Maybe a
safeHead [] = Nothing
safeHead (x:_) = Just x


-- 9. List Classification: a function that calssifies a list as empty, singleton, or a long list with pattern matching
classifyList :: [Int] -> String
classifyList [] = "Empty List"
classifyList [_] = "Singleton List"
classifyList _ = "Long List"


-- 10. Sum Pairs: a function that sums the elements of a list of pairs
sumPairs :: [(Int, Int)] -> [Int]
sumPairs xs = [fst xTup + snd xTup | xTup <- xs]


-- 11.
