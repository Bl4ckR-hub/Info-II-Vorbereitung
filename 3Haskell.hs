{-# OPTIONS_GHC -Wno-unrecognised-pragmas #-}
{-# HLINT ignore "Redundant bracket" #-}
import GHC.Generics (C)
import System.Posix (RTLDFlags)
data Signal = X | O  --Definition eines neuen Typs

instance Show Signal where      --Wir machen den neuen Typen zum Mitglied der Typklasse SHow, sodass die implementierte Methode show benutzt werden kann
    show X = "X"
    show O = "O"

instance Eq Signal where        --Wir machen den neuen Typen zum Mitglied der Typklasse Eq, sodass wir die Gleichheitsfunktionen anwenden können
    a == b = show a == show b

class UNiqq a where     --Hier gründen wir eine neue TypKLasse
    isUnique :: a -> Bool

instance UNiqq Integer where            --Hier machen wir Int zum Teil der TypKLasse
    isUnique a = a `mod` 3 == 0 && even a


class (Eq a) => X a where           --Diese Typklasse X lässt sich nur auf die Typen anwenden, die ein Teil der Typklasse Eq sind
    foo :: a -> Bool

instance X Integer where
    foo a = a `mod` 37 == 0


data Special = A | B | C            --Dieser Typ ist kein Teil der Typklasse Eq

-- instance X Special where    Wir können das nicht machen


--Wozu braucht man eingeschränkte Typ Parameter
contains :: (Eq a) => [a] -> a -> Bool
contains [] _ = False
contains (x:xs) val = x == val || contains xs val
