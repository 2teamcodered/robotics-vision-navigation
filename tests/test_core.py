from navsim.core import plan
def test_avoids_obstacle(): assert plan([[0,0],[1,0]],(0,0),(1,1))[-1] == (1,1)
