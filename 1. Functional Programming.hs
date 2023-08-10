
--Function
f :: Int -> Int
f x = x*x + x

--Operation
(==>) :: Bool -> Bool -> Bool
(==>) x y = not x || y

--Constant Function
e :: Double
e = exp 1

--f and ==> use pattern matching to calculate the output
-- Here you See the Alternatives

abs_copy :: Int -> Int
abs_copy x = if x < 0 then -x else x

--You can also use Guarded equations to represent alternatives

--exclusive or
(<+>) :: Bool -> Bool -> Bool
(<+>) x y
    | x == y = False
    | otherwise = True


--Recursion
heron :: Int -> Double -> Double
heron n x = if n > 0 then (heron (n-1) x + x / (heron (n-1) x))/2 else x

--with guarded equations
heron2 :: (Int, Double) -> Double
heron2 (n, x)
    | n < 0 = 0
    | n == 0 = x
    |otherwise = (heron2 (n-1, x) + x / heron2 (n-1, x))/2

--usage of where
heronC :: Int -> Double -> Double
heronC n a
    | n < 0 = -31415
    | n == 0 = a
    | otherwise = (x + a/x) / 2
    where
        x = heronC (n-1) a

--Fibonacci
fiboA :: Int -> Int
fiboA n
    | n < 0 = -1
    | n == 0 = 0
    | n == 1 = 1
    |otherwise = n1 + n2
    where
        n1 = fiboA (n-1)
        n2 = fiboA (n-2)

--Recursion of Operators
(<###>) :: Int -> Double -> Double
0 <###> x = x
n <###> x = (xn1 + x / xn1) / 2
    where
        xn1 = (n-1) <###> x