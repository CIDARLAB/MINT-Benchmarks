DEVICE tree_valve_test

LAYER FLOW

H BANK b1 of 4 PORT r=100 dir=DOWN spacing=1500 channelWidth=100;
H TREE m2 4 to 1 spacing=1500 flowChannelWidth=100;
PORT p1 r=100;

CHANNEL c1 from b1 1 to m2 1 w=100;
CHANNEL c2 from b1 2 to m2 2 w=100;
CHANNEL c3 from b1 3 to m2 3 w=100;
CHANNEL c4 from b1 4 to m2 4 w=100;
CHANNEL c5 from p1 1 to m2 5 w=100;

END LAYER

LAYER CONTROL

VALVE v1 on c1 w=300 l=100;
VALVE v2 on c2 w=300 l=100;
VALVE v3 on c3 w=300 l=100;
VALVE v4 on c4 w=300 l=100;

PORT cp1 r=100;

CHANNEL cc1 from v1 2 to v2 4 w=50;
CHANNEL cc2 from v2 2 to v3 4 w=50;
CHANNEL cc3 from v3 2 to v4 4 w=50;
CHANNEL cc4 from v1 4 to cp1 1 w=50;

END LAYER
