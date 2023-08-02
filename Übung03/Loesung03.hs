data Prozess = Prozess {pid :: String, arrival :: Int, computing :: Int } deriving(Show)

instance Eq Prozess where
    a == b = computing a == computing b

instance Ord Prozess where
    compare x y
        | computing x < computing y = LT
        | computing x > computing y = GT
        | otherwise = EQ

idle :: Prozess
idle = Prozess { pid = "IDLE", arrival = -1, computing = -1 }

p1 :: Prozess
p1 = Prozess {pid = "P1", arrival = 0, computing = 6}
p2 :: Prozess
p2 = Prozess {pid = "P2", arrival = 2, computing = 6}
p3 :: Prozess
p3 = Prozess {pid = "P3", arrival = 4, computing = 5}
p4 :: Prozess
p4 = Prozess {pid = "P4", arrival = 12, computing = 4}
p5 :: Prozess
p5 = Prozess {pid = "P5", arrival = 16, computing = 3}
p6 :: Prozess
p6 = Prozess {pid = "P6", arrival = 19, computing = 6}

ps :: [Prozess]
ps = [p1, p2, p3, p4, p5, p6]

lectureExample :: State
lectureExample = State {new = ps, run = idle, ready = [], time = 0, chart = ""}



data State = State {new :: [Prozess], run :: Prozess, ready :: [Prozess], time :: Int, chart :: String}

--Aufgabe 1

--Hilfsfunktion zum Ausgeben einer Liste von Prozessen
showProcessList :: [Prozess] -> String
showProcessList [] = ""
showProcessList [x] = show x
showProcessList (x:xs) = show x ++ "\n" ++ showProcessList xs

instance Show State where
    show a = "--new\n" ++ showProcessList (new a) ++ "\n--run\n" ++ show (run a) ++ "\n--ready\n" ++ showProcessList (ready a) ++ "\n--time: " ++ show (time a) ++"\n--chart: " ++ show (chart a)


--Aufgabe 2

update_ready :: State -> State
update_ready state@(State {new = []}) = state
update_ready state@(State {new = n:ns, ready = [], time = t})
    | arrival n > t = state
    | otherwise = update_ready State {new = ns, run = run state, ready = [n], time = time state, chart = chart state}
update_ready state@(State {new = n:ns, ready = r:rs, time = t})
    | arrival n > t = state
    | otherwise = update_ready State {new = ns, run = run state, ready = r:rs ++ [n], time = time state, chart = chart state}


-- Aufgabe 3
update_run :: State -> State
update_run state@(State {ready = []}) = state
update_run state@(State {ready = r:rs})
    | run state == idle = State {new = new state, run = r, ready = rs, time = time state, chart = chart state}
    | otherwise = state

--Aufgabe 4
update_time :: State -> State
update_time state@(State {run = running})
    | computing running < 1 = State {new = new state, run = idle, ready = ready state, time = time state + 1, chart = ""}
    | otherwise = State {new = new state, run = updated, ready = ready state, time = time state + 1, chart = pid updated}
    where
        updated = Prozess {pid = pid running, arrival = arrival running, computing = computing running - 1}

--Aufgabe 5
fcfs_update_status :: State -> State
fcfs_update_status state
    | null (new state) && null (ready state) && run state == idle = state
    | otherwise = fcfs_update_status (update_time (update_run (update_ready state)))