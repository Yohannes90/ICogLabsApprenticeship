{-|
Haskell Notes
-}

-- Import necessary libraries
import Data.List
import System.IO

-- Constants for maximum and minimum Int values
maxInt = maxBound :: Int
minInt = minBound :: Int

-- Numeric types: Int, Integer, Float, Double
bigFloat :: Double
bigFloat = 3.99999 + 0.33333

-- Example of type annotation
always5 :: Int
always5 = 5

-- Basic operations
addEx = 4 + 4
subEx = 3 - 1

-- Custom addition function
add' :: Int -> Int -> Int
add' x y = x + y

-- Logical operations
trueAndFalse = True && False
trueOrFalse = True || False
notTrue = not True

-- Lists and list operations
primeNumbers = [3, 5, 7, 11]
morePrimeNumbers = primeNumbers ++ [13, 17, 19, 23, 29]
favNums = 2 : 7 : 66 : []

multiList = [[3, 5, 7], [11, 13, 17]]
lenPrime = length morePrimeNumbers
revPrime = reverse morePrimeNumbers
isListEmpty = null morePrimeNumbers
byIndexPrime = morePrimeNumbers !! 2
firstPrime = head morePrimeNumbers
restOfPrime = tail morePrimeNumbers
lastPrime = last morePrimeNumbers
first3Primes = take 3 morePrimeNumbers

-- Ranges and list comprehensions
zeroToTen = [0 .. 10]
evenList = [2, 4 .. 30]
letterList = ['A', 'B' .. 'Z']
listTimes2 = [x * 2 | x <- [1..10], x * 2 <= 12]
divisibleBy13 = [x | x <- [1..100], x `mod` 13 == 0]
divisibleBy13N9 = [x | x <- [1..500], x `mod` 13 == 0, x `mod` 9 == 0]

-- Sorting and filtering
sortedList = sort [3, 1, 6, 2, 1, 0, 7, 4]
listBiggerThan5 = filter (> 5) sortedList

-- Higher-order functions
listTimes4 = map (* 4) [1..5]
multBy5 :: [Int] -> [Int]
multBy5 [] = []
multBy5 (x:xs) = (x * 5) : multBy5 xs

-- Folds
multOfList = foldl (*) 1 [2, 3, 4, 5]  -- 120
sumOfList = foldr (+) 0 [1, 2, 3, 4, 5]  -- 15

-- Tuples
derekBanas = ("Derek Banas", 52)
derekName = fst derekBanas
derekAge = snd derekBanas

-- Zipping lists
names = ["Yohannes", "Kebede", "Kelele"]
age = [23, 53, 42]
namesNages = zip names age

-- Functions and pattern matching
addMe :: Int -> Int -> Int
addMe x y = x + y

whatAge :: Int -> String
whatAge 16 = "You can drive"
whatAge 18 = "You can vote"
whatAge 21 = "You're an adult"
whatAge _  = "Nothing important"

factorial :: Int -> Int
factorial 0 = 1
factorial n = n * factorial (n - 1)

-- Guards
isOdd :: Int -> Bool
isOdd n
    | n `mod` 2 == 0 = False
    | otherwise      = True

whatGrade :: Int -> String
whatGrade age
    | age >= 5 && age <= 6  = "Kindergarten"
    | age >= 6 && age <= 10 = "Elementary School"
    | age >= 10 && age <= 14 = "Middle School"
    | age >= 14 && age <= 18 = "High School"
    | age >= 18 && age <= 25 = "University or College"
    | otherwise             = "Work or Other"

-- Case expressions
getActivity :: Int -> String
getActivity n = case n of
    5 -> "Workout"
    6 -> "Read Philosophy"
    7 -> "Read relevant papers"
    8 -> "Meditate"
    _ -> "Sleep"

-- Data types and type classes
data BaseballPlayer = Pitcher | Catcher | Infielder | Outfield deriving Show

barryBonds :: BaseballPlayer -> Bool
barryBonds Outfield = True
barryInOf = barryBonds Outfield

-- Custom data types
data Customer = Customer String String Double deriving Show

tomSmith :: Customer
tomSmith = Customer "Tom Smith" "123 Main" 20.50

getBalance :: Customer -> Double
getBalance (Customer _ _ b) = b

-- Recursive functions
multBy4 :: [Int] -> [Int]
multBy4 [] = []
multBy4 (x:xs) = (x * 4) : multBy4 xs

-- Lambdas
dbl1to10 = map (\x -> x * 2) [1..10]
sqrList = map (\x -> x ^ 2) [1..10]

-- Custom shapes with pattern matching
data Shape = Circle Float Float Float | Rectangle Float Float Float Float deriving Show

area :: Shape -> Float
area (Circle _ _ r) = pi * r ^ 2
area (Rectangle x y x2 y2) = (x2 - x) * (y2 - y)

-- Main function example
main :: IO ()
main = do
    putStrLn "What is your name?"
    name <- getLine
    putStrLn ("Hello, " ++ name ++ "!")
