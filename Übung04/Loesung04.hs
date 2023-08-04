{-# OPTIONS_GHC -Wno-unrecognised-pragmas #-}
{-# HLINT ignore "Use camelCase" #-}
import Data.Maybe

parabolaRootB :: Double -> Double -> Maybe (Double, Double)
parabolaRootB p q
    | y < 0 = Nothing
    | otherwise = Just (-x + sqrt y, -x - sqrt y)
    where
        x = p/2.0
        y = x*x - q


--Aufgabe 1
err :: error
err = error "Not correct Input"


match :: String -> [String] -> [String]
match _ [] = err
match val (l:ls)
    | val /= l = err
    | otherwise = ls

id_list :: [String] -> [String]
id_list [] = err
id_list (x:xs) = id_list_tail (match "id" (x:xs))

id_list_tail :: [String] -> [String]
id_list_tail [] = err
id_list_tail (x:xs)
    | x == "," = id_list_tail (match "id" (match "," (x:xs)))
    | otherwise = match "$$" (match ";" (x:xs))


--Aufgabe 2
match1 :: Char -> Maybe String -> Maybe String
match1 _ Nothing = Nothing
match1 char (Just "") = Nothing
match1 char (Just (x:xs))
    | char == x = Just xs
    | otherwise = Nothing

prog :: String -> Maybe String
prog args = match1 '$' (expr (Just args))

expr :: Maybe String -> Maybe String
expr args = ttail (term args)

term :: Maybe String -> Maybe String
term args = ftail (factor args)

ttail :: Maybe String -> Maybe String
ttail args
    | isJust (match1 '+' args) = ttail (term (match1 '+' args))
    | otherwise = args

factor :: Maybe String -> Maybe String
factor = match1 'c'             --wenn 2 Funktionen gleiche Argumente nehmen, einfach skippen

ftail :: Maybe String -> Maybe String
ftail args
    | isJust (match1 '*' args) = ftail (factor (match1 '*' args))
    | otherwise = args




