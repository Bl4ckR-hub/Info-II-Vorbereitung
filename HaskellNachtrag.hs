contains :: (Eq a) => [a] -> a -> Bool
contains [] _ = False
contains (x:xs) y = x == y || contains xs y



--Exklusives Oder
(<+>) :: Bool -> Bool -> Bool
x <+> y = (x || y) && not (x && y)

--Testen
tableRow :: (Bool -> Bool -> Bool) -> (Bool, Bool) -> String
tableRow op (a,b) = show (a,b) ++ " = " ++ show (op a b)

table :: (Bool -> Bool -> Bool) -> [(Bool, Bool)] -> String
table _ [] = ""
table f (x:xs) =  "\n" ++ tableRow f x ++ table f xs


main = do
    let li = [(True, False), (False, True), (True, True), (False, False)]
    putStrLn (table (<+>) li)
    let conc = [False, False] ++ [True, True]
    print conc
--To concatlists, use the ++ operator

--You can also use the head, tail and null functions in haskell
tableAlternative :: (Bool -> Bool -> Bool) -> [(Bool, Bool)] -> String
tableAlternative f li
    | null li = ""
    | otherwise = tableRow f (head li) ++ "\n" ++ tableAlternative f (tail li)

--In haskell, you can use Composition of nfunctions with the . operator
nor :: [Bool] -> Bool
nor = not.or

--Nun können wir die Gleichheit von Bits realisieren

type Nibble = (Bool, Bool, Bool, Bool)

equals :: Nibble -> Nibble -> Bool
equals (x4, x3, x2, x1) (y4, y3, y2, y1) = nor [x4 <+> y4, x3 <+> y3, x2 <+> y2, x1 <+> y1]


