DEVICE net_test

LAYER FLOW
PORT p1, p2 r=100;
V LONG CELL TRAP ct1 numChambers=10 chamberWidth=100 chamberLength=100 chamberSpacing=50 channelWidth=100;

CHANNEL c1 from p1 3 to ct1 1 w=100;
CHANNEL c2 from ct1 2 to p2 1 w=100;

END LAYER

LAYER CONTROL
PORT p3 r=100;
VALVE v1 on c1 w=300 l=100;
VALVE v2 on c2 w=300 l=100;
NET net1 from p3 1 to v1 4, v2 4 channelWidth=50;
END LAYER
