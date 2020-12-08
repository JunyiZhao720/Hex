from spark.HexEngine import HexEngine

# Testing encoding decoding
engine = HexEngine(n = 8, player1 = None, player2 = None, gui = None, player1First = True)

# decoding
assert engine._decodePoint(0) == (1, 1),   engine._decodePoint(0)
assert engine._decodePoint(7) == (1, 8),   engine._decodePoint(7)
assert engine._decodePoint(16) == (3, 1),  engine._decodePoint(16)
assert engine._decodePoint(19) == (3, 4),  engine._decodePoint(19)
assert engine._decodePoint(22) == (3, 7),  engine._decodePoint(22)
assert engine._decodePoint(24) == (4, 1),  engine._decodePoint(24)
assert engine._decodePoint(30) == (4, 7),  engine._decodePoint(30)
assert engine._decodePoint(31) == (4, 8),  engine._decodePoint(31)
assert engine._decodePoint(39) == (5, 8),  engine._decodePoint(39)
assert engine._decodePoint(63) == (8, 8),  engine._decodePoint(63)

# encoding
assert engine._encodePoint(coordinate=(1,1)) == 0,  engine._encodePoint(coordinate=(1,1))
assert engine._encodePoint(coordinate=(1,8)) == 7,  engine._encodePoint(coordinate=(1,8))
assert engine._encodePoint(coordinate=(3,1)) == 16, engine._encodePoint(coordinate=(3,1))
assert engine._encodePoint(coordinate=(3,4)) == 19, engine._encodePoint(coordinate=(3,4))
assert engine._encodePoint(coordinate=(3,7)) == 22, engine._encodePoint(coordinate=(3,7))
assert engine._encodePoint(coordinate=(4,1)) == 24, engine._encodePoint(coordinate=(4,1))
assert engine._encodePoint(coordinate=(4,7)) == 30, engine._encodePoint(coordinate=(4,7))
assert engine._encodePoint(coordinate=(4,8)) == 31, engine._encodePoint(coordinate=(4,8))
assert engine._encodePoint(coordinate=(5,8)) == 39, engine._encodePoint(coordinate=(5,8))
assert engine._encodePoint(coordinate=(8,8)) == 63, engine._encodePoint(coordinate=(8,8))

# Testing adj nodes
assert engine._adjNodes(point=0)   == [1, 8, 9],                 engine._adjNodes(point=0)
assert engine._adjNodes(point=3)   == [2, 4, 11, 12],            engine._adjNodes(point=3)
assert engine._adjNodes(point=11)  == [2, 3, 10, 12, 19, 20],    engine._adjNodes(point=11)
assert engine._adjNodes(point=15)  == [6, 7, 14, 23],            engine._adjNodes(point=15)
assert engine._adjNodes(point=7)   == [6, 15],                   engine._adjNodes(point=7)
