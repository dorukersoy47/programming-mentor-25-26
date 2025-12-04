-- foldr version
foldr_ :: (a -> b -> b) -> b -> [a] -> b
foldr_ op z [ ] = z
foldr_ op z (x : xs) = op x (foldr_ op z xs)

-- foldr1 version
foldr1_ :: (a -> a -> a) -> [a] -> a  
foldr1_ op [x] = x
foldr1_ op (x:xs) = op x (foldr1_ op xs)

-- foldl version
foldl_ :: (b -> a -> b) -> b -> [a] -> b
foldl_ op z [ ] = z
foldl_ op z (x : xs) = foldl_ (op) (op z x) xs

-- foldl1 version
foldl1_ :: (a -> a -> a) -> [a] -> a
foldl1_ op [x] = x
foldl1_ op (x:y:xs) = foldl1_ (op) ((op x y) : xs) 