{-# OPTIONS_GHC -Wno-unrecognised-pragmas #-}
import Distribution.Simple.Utils (xargs)
import Data.Maybe
import Distribution.Simple.Register (inplaceInstalledPackageInfo)
{-# HLINT ignore "Use camelCase" #-}

-- Aufgabe 1

message = "Wrong Input"


match :: String -> [String] -> [String]
match _ [] = error message
match a (x:xs)
    | a == x = xs
    | otherwise = error message

id_list :: [String] -> [String]
id_list (x:xs) = id_list_tail (match "id" (x:xs))

id_list_tail :: [String] -> [String]
id_list_tail [] = match "a" []
id_list_tail (x:xs)
    | x == "," = id_list_tail (match "id" (match "," (x:xs)))
    | otherwise = match "$$" (match ";" (x:xs))

-- Aufgabe 2

match2 :: Char -> Maybe String -> Maybe String
match2 _ (Just "") = Nothing
match2 _ Nothing = Nothing
match2 ch (Just (x:xs))
    | ch == x = Just xs
    | otherwise = Nothing

prog :: String -> Maybe String
prog inp = match2 '$' (expr (Just inp))

expr :: Maybe String -> Maybe String
expr inp = ttail (term inp)

term :: Maybe String -> Maybe String
term inp = ftail (factor inp)

ttail :: Maybe String -> Maybe String
ttail inp
    | isNothing (match2 '+' inp) = inp
    | otherwise = ttail (term (match2 '+' inp))

factor :: Maybe String -> Maybe String
factor inp = match2 'c' inp

ftail :: Maybe String -> Maybe String
ftail inp 
    | isNothing (match2 '*' inp) = inp
    | otherwise =  ftail (factor (match2 '*' inp)) 


    