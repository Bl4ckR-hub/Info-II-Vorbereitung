--Aufgabe 1
type Nibble = (Bool, Bool, Bool, Bool)

--Hilfsfunktion
showBooltoBin :: Bool -> Char
showBooltoBin True = '1'
showBooltoBin False = '0'

--Hilfsfunktion
nibbleToBin :: Nibble -> String
nibbleToBin (a,b,c,d) = [showBooltoBin a, showBooltoBin b, showBooltoBin c, showBooltoBin d]

--Hilfsfunktion
stringBinToPosDec :: String -> Int
stringBinToPosDec [] = 0
stringBinToPosDec (x:xs) = if x == '0' then stringBinToPosDec xs else pow2 (length xs) + stringBinToPosDec xs

--Hilfsfunktion
stringBinInvert :: String -> String
stringBinInvert [] = ""
stringBinInvert (x:xs) = if x == '0' then "1" ++ stringBinInvert xs else "0" ++ stringBinInvert xs

--Hilfsfunktion
stringBinToNegDec :: String -> Int
stringBinToNegDec [] = -1
stringBinToNegDec (x:xs) = if x == '0' then stringBinToNegDec xs else (-1)*pow2(length xs) + stringBinToNegDec xs

--Hilfsfunktion
pow2 :: Int -> Int
pow2 0 = 1
pow2 1 = 2
pow2 n = if (n `mod` 2) == 0 then pow2(n `div` 2) * pow2 (n `div` 2) else 2 * pow2((n-1)`div` 2) * pow2((n-1)`div` 2)


showNibble :: Nibble -> String
showNibble nibble = string ++ posbin ++ negbin
    where
        string = nibbleToBin nibble
        posbin = "   " ++ show (stringBinToPosDec string)
        negbin = "   " ++ show (stringBinToNegDec (stringBinInvert string))

--Aufgabe 2
bitAdder :: Bool -> Bool -> Bool -> (Bool, Bool)
bitAdder x y z = (c,s)
    where
        c = c' || c''
        c' = x && y
        c'' = s' && z
        s' = x /= y
        s = s' /= z

--Aufgabe 3
nibbleAdder :: Nibble -> Nibble -> (Bool, Nibble)
nibbleAdder (x3, x2, x1, x0) (y3, y2, y1, y0) =(c,(s3,s2,s1,s0))
    where
        c1 = fst (bitAdder x0 y0 False)
        s0 = snd (bitAdder x0 y0 False)
        c2 = fst (bitAdder x1 y1 c1)
        s1 = snd (bitAdder x1 y1 c1)
        c3 = fst (bitAdder x2 y2 c2)
        s2 = snd (bitAdder x2 y2 c2)
        c = fst (bitAdder x3 y3 c3)
        s3 = snd (bitAdder x3 y3 c3)

--Aufgabe 4
tableAdder :: (Nibble -> Nibble -> (Bool, Nibble)) -> [(Nibble, Nibble)] -> String
tableAdder func (x:xs) = showNibble a ++ "   +   " ++ showNibble b ++ "  =  " ++ c ++ "  " ++ d ++ next
    where
        a = fst x
        b = snd x
        c = show (fst (nibbleAdder a b))
        d = showNibble (snd (nibbleAdder a b))
        next = if xs /= [] then "\n" ++ tableAdder func xs else ""