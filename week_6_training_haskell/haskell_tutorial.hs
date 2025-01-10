import Data.List
import System.IO


maxInt = maxBound :: Int
minInt = minBound :: Int

-- Int
-- Integer
-- Float
-- Double
-- Bool
-- Char
-- Tuple - most times going to contain 2 values
bigFloat = 3.99999 + 0.33333

always5 :: Int
always5 = 5

sumOfNums = sum [1..5]

addEx = 4 + 4
subEx = 3 - 1

add' :: Int -> Int -> Int
add' x y = x + y

-- functions
-- pi, exp, log, truncate, round, ceiling, floor

-- more
-- sin, cos, tan, asin, atan, acos, sinh, tanh, cosh, asinh, atan, acosh

trueAndFalse = True && False
trueOrFalse = True || False
notTrue = not(True)


primeNumbers = [3, 5, 7, 11]
morePrimeNumbers = primeNumbers ++ [13, 17, 19, 23, 29]
favNums = 2 : 7 : 66 : []

morePrimes = 2 : 3 : primeNumbers


multiList = [[3, 5, 7], [11, 13, 17]]

lenPrime = length morePrimes
revPrime = reverse morePrimes

isListEmpty = null morePrimes

byIndexPrime = morePrimes !! 2
firstprime = head morePrimes
restOfPrime = tail morePrimes
lastPrime = last morePrimes

first3Primes = take 3 morePrimes



zeroToTen = [0 .. 10]
evenList = [2, 4 .. 30]
letterList = ['A', 'B' .. 'Z']

infinite = [1000000, 1000000000 ..]
many0s = take 20 (repeat 0)
many3s = replicate 10 3
cycleList = take 10 (cycle [1..3])

listTimes2 = [x * 2 | x <- [1..10], x * 2 <= 12]


divisibleBy13 = [x | x <- [1..100], x `mod` 13 == 0]

divisibleBy13N9 = [x | x <- [1..500], x `mod` 13 == 0, x `mod` 9 == 0]
divisibleBy13N92 = [x | x <- [1..500], x `mod` (13 * 9) == 0]


sortedList = sort [3, 1, 6, 2, 1, 0, 7, 4]
sumOfLists = zipWith (+) sortedList (reverse sortedList)


listBiggerThan5 = filter (> 5) sumOfLists

evenTo20 = takeWhile ( <= 20) [2, 4 ..]

-- foldl similar to js reduce high order function
-- the format: foldl (operator) accumlator [List]
multOfList = foldl (*) 1 [2, 3, 4, 5] -- 120
sumOfList = foldr (+) 0 [1, 2, 3, 4, 5] -- 15

-- note
-- (+) :: Num a => a -> a -> a
-- This means that + is a function that takes two arguments of type a and returns a value of type a, but with the constraint that a must be an instance of the Num type class.



-- List Operations

pow3List = [3^n | n <- [1..10]]

mulTable = [[x * y | y <- [1..12]] | x <- [1..12]]

randTuple = (1, "Random Tuple")

derekBanas = ("Derek Banas", 52)

derekName = fst derekBanas
derekAge = snd derekBanas


names = ["Zoro", "Saski", "Uciha"]
age = [23, 53, 42]
namesNages = zip names age

-- This works on the ghc
-- let num7 =  7
-- let getTriple x = x * 3
-- getTriple num7


--main = do
--    putStrLn "What is your name?"
--    name <- getLine
--    putStrLn ("Hello " ++ name)

-- funcName param1 param2 = opeations (returned vallue)
addMe :: Int -> Int -> Int
addMe x y = x + y

sumME x y = x + y

addTuples :: (Int, Int) -> (Int, Int) -> (Int, Int)
addTuples (a, b) (c, d) = (a + c, b + d)


whatAge :: Int -> String
whatAge 16 = "You can drive"
whatAge 18 = "You can vote"
whatAge 21 = "You're an adult"
whatAge _ = "Nothing Impotrant"



factorial :: Int -> Int
factorial 0 = 1
factorial n = n * factorial (n - 1)

-- 3 * fac (2)
-- 2 * fac (1)
-- 1 * fac (0)
-- 1 * 1
-- 2 * 1
-- 3 * 2

prodFactorial n = product [1..n]

-- 1 * 2 * 3



-- Guards

isOdd :: Int -> Bool
isOdd n
    | n `mod` 2 == 0 = False
    | otherwise = True

isEven n = n `mod` 2 == 0


whatGrade :: Int -> String
whatGrade age
    | (age >= 5) && (age <= 6) = "Kindergarten"
    | (age >= 6) && (age <= 10) = "Elementary School"
    | (age >= 10) && (age <= 14) = "Middle School"
    | (age >= 14) && (age <= 18) = "High School"
    | (age >= 18) && (age <= 25) = "University or College"
    | otherwise = "Work or Other"



batAvgRating :: Double -> Double -> String

batAvgRating hits atBats
    | avg <= 0.200 = "Terrible Batting Average"
    | avg <= 0.250 = "Average Player"
    | avg <= 0.280 = "Amazing"
    | otherwise = "You're a superstar"
    where avg = hits / atBats


getListItems :: [Int] -> String
getListItems [] = "Your list is empty"
getListItems (x:[]) = "Your list starts with " ++ show x
getListItems (x:y:[]) = "Your list contains " ++show x ++ " " ++ show y
getListItems (x:xs) = "Your list starts with " ++ show x ++ " and followed by " ++ show xs



getFirstItem :: String -> String
getFirstItem [] = "Empty String"
getFirstItem all@(x:xs) = "The first letter in " ++ all ++ " is " ++ [x]




-- High Order Functions

times4 :: Int -> Int
times4 x = x * 4

listTimes4 = map times4 [1..5]

multBy4 :: [Int] -> [Int]
multBy4 list = map times4 list




multBy5 :: [Int] -> [Int]
multBy5 [] = []
multBy5 (x:xs) = times4 x : multBy5 xs

-- [1,2,3,4] : x = 1 | xs = [2,3,4]
-- [2,3,4] : x = 2 | xs = [3,4]
-- [3,4] : x = 3 | xs = [4]
-- [4] : x = 4 | xs = []


areStringEq :: [Char] -> [Char] -> Bool
areStringEq [] [] = True
areStringEq (x:xs) (y:ys) = x == y && areStringEq xs ys
areStringEq _ _ = False


times3 :: Int -> Int
times3 x = x * 4

doMult :: (Int -> Int) -> Int
doMult func = func 3

num3times3 = doMult times3



-- how ot rerurn a function from a function
getAddFunc :: Int -> (Int -> Int)
getAddFunc x y = x + y

adds3 = getAddFunc 3
fourPlus3 = adds3 4


threePlusList = map adds3 [1, 2, 3, 4, 5]


-- Lamdas: creating functions that don't have a name


dbl1to10 = map (\x -> x * 2) [1..10]

tenPlusList = map (\x -> x + 10) [1..10]
sqrList = map (\x -> x * x) [1..10]


-- Conditionals

-- comparison operators <, >, <=, >=, ==. /=
-- logical operators &&, ||, not

doubleEvenNumber y =
    if (y `mod` 2 /= 0)
        then y
        else y * 2

getActivity :: Int -> String
getActivity n = case n of
    5 -> "Workout"
    6 -> "Read Philosopy, Literature"
    7 -> "Read relevant papers"
    8 -> "Meditate"
    _ -> "Sleep"


-- modules
-- module SampFunctions (getAcitvity, doubleEvenNumber) where
-- import SampFunctions


-- Enumerations
data BaseballPlayer = Pitcher
                    | Catcher
                    | Infielder
                    | Outfield
                deriving Show

barryBonds :: BaseballPlayer -> Bool
barryBonds Outfield = True

barryInOf = print(barryBonds Outfield)


data Customer = Customer String String Double
    deriving Show

tomSmith :: Customer
tomSmith = Customer "Tom Smith" "123 Main" 20.50

getBalance :: Customer -> Double
getBalance (Customer _ _ b) = b



data RPS = Rock | Paper | Scissors

shoot :: RPS -> RPS -> String
shoot Paper Rock = "Paper Beats Rock"
shoot Rock Scissors = "Rock Beats Scissors"
shoot Scissors Paper = "Scissors Beats Paper"
shoot Rock Paper = "Paper Beats Rock"
shoot Scissors Rock = "Rock Beats Scissors"
shoot Paper Scissors = "Scissors Beats Paper"
shoot _ _ = "It's a tie"


data Shape = Circle Float Float Float | Rectangle Float Float Float Float
    deriving Show

area :: Shape -> Float
area (Circle _ _ r) = pi * r ^ 2
area (Rectangle x y x2 y2) = (abs (x2 - x)) * (abs (y2 - y))
-- equivalent to the above, just replaced the brackt annotation with $ sign
-- area (Rectangle x y x2 y2) = (abs $ x2 - x) * (abs $ y2 - y)

sumValue = putStrLn $ show $ 1 + 2
sumValue2 = putStrLn . show $ 1 + 2

areaOfCircle = area (Circle 50 60 20)
areaOrRect = area (Rectangle 10 10 100 100)



-- Type Classes
-- Num, Eq, Show

data Employee = Employee { name :: String,
                            position :: String,
                            idNum :: Int
                        } deriving (Eq, Show)
samSmith = Employee {name = "Sam Smith", position = "Manager", idNum = 1000}
pamMarx = Employee {name = "Pam Marx", position = "Sales", idNum = 1001}

isSamPam = samSmith == pamMarx

samSmithData = show samSmith


-- Type Instances

-- data ShirtSize = S | M | L
-- instance Eq ShirtSize where
--     S == S = True
--     M == M = True
--     L == L = True
--     _ == _ = False

-- instance Show ShirtSize where
--     show S = "Small"
--     show M = "Medium"
--     show L = "Large"

-- smallAvail = S `elem` [S, M, L]

-- theSize = show S




-- Custom Type Class
class MyEq a where
    areEqual :: a -> a -> Bool

data ShirtSize = S | M | L

instance MyEq ShirtSize where
    areEqual S S = True
    areEqual M M = True
    areEqual L L = True
    areEqual _ _ = False

newSize = areEqual M M


-- Quick review on getting input and then output
sayHello = do
    putStrLn "What is your name?"
    name <- getLine
    putStrLn $ "Hello " ++ name

-- File IO
-- write to a file

writeToFile = do
    theFile <- openFile "test.txt" WriteMode
    hPutStrLn theFile ("Random line of to be written to file")
    hClose theFile

-- read to a file

readFromFile = do
    theFile2 <- openFile "test.txt" ReadMode
    contents <- hGetContents theFile2
    putStr contents
    hClose theFile2

-- a bit confusing implementation of a function generating a fibnachii series
-- fib = 1 : 1 : [a + b ! (a, b) <- zip fib (tail fib)]


doubleSmallNumber :: Int -> Int
doubleSmallNumber x = if x < 100
                        then x * 2
                        else x

doubleSmallNumberAdd :: Int -> Int
doubleSmallNumberAdd x = (if x < 100 then x * 2 else x) + 1

-- spaced repetition W active recall

-- someFunc x = x ** 2

-- mymap :: (a -> b) -> [a] -> [b]
-- mymap func list = [func x | x <- list]




-- module Main where
main :: IO ()
main = putStrLn "Hello, World!"
