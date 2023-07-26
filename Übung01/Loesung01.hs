import Data.Char (toLower)

--Aufgabe 1
quadratic :: (Int, Int, Int) -> Int -> Int --Declaring Function
quadratic (a, b, c) x = a*x*x + b*x + c    --Defining Function
-------------------------------------------------------------
square :: Int -> Int
square n
    | n < 0 = square (-n)
    | n == 0 = 0
    | otherwise = sum
    where sum = 2*n - 1 + square (n-1)
-------------------------------------------------------------
sumList :: [Int] -> Int
sumList [] = 0
sumList (x:xs) = x + sumList xs

foldList :: (Double -> Double -> Double) -> [Double] -> Double
foldList op [x] = x
foldList op [] = 0
foldList op (x:xs) = op x (foldList op xs)
-------------------------------------------------------------
mapList :: (Int -> Int) -> [Int] -> [Int]
mapList func [] = []
mapList func (x:xs) = [func x] ++ mapList func xs
-------------------------------------------------------------
tableInt :: (Int -> Int) -> [Int] -> String
tableInt func [] = ""
tableInt func [x] = show x ++ ":" ++ show (func x)
tableInt func (x:xs) = show x ++ ":" ++ show (func x) ++ "\n" ++ (tableInt func xs)


--Aufgabe 2
containsList :: [Int] -> Int -> Bool
containsList [] num = False
containsList (x:xs) num = x == num || containsList xs num
-------------------------------------------------------------
countList :: [Char] -> Char -> Int
countList [] char = 0
countList (c:cs) char = if (toLower c) == (toLower char) then 1 + (countList cs char) else countList cs char
