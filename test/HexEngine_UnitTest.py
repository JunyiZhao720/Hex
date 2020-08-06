from HexEngine import HexEngine

# Testing encoding decoding
engine = HexEngine.create_new(n=8,human_color_red=True,human_move_first=True,gui=None,ai=None)

# decoding
assert engine._decode_point(0) == (1, 1),   engine._decode_point(0)
assert engine._decode_point(7) == (1, 8),   engine._decode_point(7)
assert engine._decode_point(16) == (3, 1),  engine._decode_point(16)
assert engine._decode_point(19) == (3, 4),  engine._decode_point(19)
assert engine._decode_point(22) == (3, 7),  engine._decode_point(22)
assert engine._decode_point(24) == (4, 1),  engine._decode_point(24)
assert engine._decode_point(30) == (4, 7),  engine._decode_point(30)
assert engine._decode_point(31) == (4, 8),  engine._decode_point(31)
assert engine._decode_point(39) == (5, 8),  engine._decode_point(39)
assert engine._decode_point(63) == (8, 8),  engine._decode_point(63)

# encoding
assert engine._encode_point(coordinate=(1,1)) == 0,  engine._encode_point(coordinate=(1,1))
assert engine._encode_point(coordinate=(1,8)) == 7,  engine._encode_point(coordinate=(1,8))
assert engine._encode_point(coordinate=(3,1)) == 16, engine._encode_point(coordinate=(3,1))
assert engine._encode_point(coordinate=(3,4)) == 19, engine._encode_point(coordinate=(3,4))
assert engine._encode_point(coordinate=(3,7)) == 22, engine._encode_point(coordinate=(3,7))
assert engine._encode_point(coordinate=(4,1)) == 24, engine._encode_point(coordinate=(4,1))
assert engine._encode_point(coordinate=(4,7)) == 30, engine._encode_point(coordinate=(4,7))
assert engine._encode_point(coordinate=(4,8)) == 31, engine._encode_point(coordinate=(4,8))
assert engine._encode_point(coordinate=(5,8)) == 39, engine._encode_point(coordinate=(5,8))
assert engine._encode_point(coordinate=(8,8)) == 63, engine._encode_point(coordinate=(8,8))

# Testing adj nodes
engine = HexEngine.create_new(n=8,human_color_red=True,human_move_first=True,gui=None,ai=None)

assert engine._adj_nodes(point=0)   == [1, 8, 9],                 engine._adj_nodes(point=0)
assert engine._adj_nodes(point=3)   == [2, 4, 11, 12],            engine._adj_nodes(point=3)
assert engine._adj_nodes(point=11)  == [2, 3, 10, 12, 19, 20],    engine._adj_nodes(point=11)
assert engine._adj_nodes(point=15)  == [6, 7, 14, 23],            engine._adj_nodes(point=15)
assert engine._adj_nodes(point=7)   == [6, 15],                   engine._adj_nodes(point=7)
