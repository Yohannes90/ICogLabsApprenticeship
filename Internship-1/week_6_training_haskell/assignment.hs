-- Checkout chapter 2 4 and 5
-- https://learnyouahaskell.github.io/higher-order-functions.html#maps-and-filters

-- Tasks:
-- map, filter, foldl, foldr, sum, product, count, compose

-- 1. map
map' :: (a -> b) -> [a] -> [b]
map' func xs = [func x | x <- xs]

-- map' (*2) [1, 2, 3]         -- [2, 4, 6]


-- 2. filter
filter' :: (a -> Bool) -> [a] -> [a]
filter' func xs = [x | x <- xs, func x]

-- filter' even [1, 2, 3, 4]   -- [2, 4]


-- 3. foldl
foldl' :: (b -> a -> b) -> b -> [a] -> b
foldl' _ z [] = z
foldl' func z (x:xs) = foldl' func (func z x) xs

-- foldl' (+) 0 [1, 2, 3]      -- 6


-- 4. foldr
foldr' :: (a -> b -> b) -> b -> [a] -> b
foldr' _ z [] = z
foldr' func z (x:xs) = func x (foldr' func z xs)

-- foldr' (+) 0 [1, 2, 3]      -- 6


-- 5. sum
sum' :: Num a => [a] -> a
sum' [] = 0
sum' (x:xs) = x + sum' xs

-- sum' [1, 2, 3]              -- 6


-- 6. product
product' :: Num a => [a] -> a
product' [] = 1
product' (x:xs) = x * product' xs

-- product' [1, 2, 3]          -- 6


-- 7. count
count' :: [a] -> Int
count' [] = 0
count' (_:xs) = 1 + count' xs

-- count' [1, 2, 3]            -- 3


length' :: [a] -> Int
length' [] = 0
length' xs = sum' [1 | _ <- xs]

-- length' [1, 2, 3]           -- 3

-- 7.2. count occurence of a given int in a list
countOccerence :: [Int] -> Int -> Int
countOccerence [] _ = 0
countOccerence xs z = sum' [1 | x <- xs, x == z]

-- countOccerence (2:2:[2..5]) 2       -- 3

-- 8. compose
-- note: In Haskell, compose refers to the composition of two functions.
    -- Function composition allows you to combine two or more functions into a single function.
    -- It is represented by the operator (.) in Haskell, (.) :: (b -> c) -> (a -> b) -> a -> c
compose' :: (b -> c) -> (a -> b) -> (a -> c)
compose' f g = \x -> f (g x)

-- compose' not even 3         -- True

double :: Int -> Int
double x = x * 2

increment :: Int -> Int
increment x = x + 1

-- compose' double increment 10     -- 22
-- compose' increment double 10     -- 21
