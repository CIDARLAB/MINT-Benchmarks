DEVICE grid_4_mixer

LAYER FLOW
H TREE m1 1 to 4 spacing=1200 flowChannelWidth=100;
V MIXER n1 numBends=10 bendSpacing=100 bendLength=500 channelWidth=100;
V MIXER n2 numBends=10 bendSpacing=100 bendLength=500 channelWidth=100;
V MIXER n3 numBends=10 bendSpacing=100 bendLength=500 channelWidth=100;
V MIXER n4 numBends=10 bendSpacing=100 bendLength=500 channelWidth=100;
H TREE m2 4 to 1 spacing=1200 flowChannelWidth=100;
PORT p1, p2 r=100;
SQUARE CELL TRAP ct1, ct2, ct3, ct4, ct5, ct6, ct7, ct8, ct9, ct10, ct11, ct12, ct13, ct14, ct15, ct16 chamberWidth=100 chamberLength=100 channelWidth=100;

CHANNEL c1 from p1 3 to m1 1 w=100;
CHANNEL c2 from m1 2 to n1 1 w=100;
CHANNEL c3 from m1 3 to n2 1 w=100;
CHANNEL c4 from m1 4 to n3 1 w=100;
CHANNEL c5 from m1 5 to n4 1 w=100;

CHANNEL c2b from n1 2 to ct1 1 w=100;
CHANNEL c3b from n2 2 to ct2 1 w=100;
CHANNEL c4b from n3 2 to ct3 1 w=100;
CHANNEL c5b from n4 2 to ct4 1 w=100;

CHANNEL c6 from ct1 2 to ct2 4 w=100;
CHANNEL c7 from ct2 2 to ct3 4 w=100;
CHANNEL c8 from ct3 2 to ct4 4 w=100;

CHANNEL c9 from ct1 3 to ct5 1 w=100;
CHANNEL c10 from ct2 3 to ct6 1 w=100;
CHANNEL c11 from ct3 3 to ct7 1 w=100;
CHANNEL c12 from ct4 3 to ct8 1 w=100;

CHANNEL c13 from ct5 2 to ct6 4 w=100;
CHANNEL c14 from ct6 2 to ct7 4 w=100;
CHANNEL c15 from ct7 2 to ct8 4 w=100;

CHANNEL c16 from ct5 3 to ct9 1 w=100;
CHANNEL c17 from ct6 3 to ct10 1 w=100;
CHANNEL c18 from ct7 3 to ct11 1 w=100;
CHANNEL c19 from ct8 3 to ct12 1 w=100;

CHANNEL c20 from ct9 2 to ct10 4 w=100;
CHANNEL c21 from ct10 2 to ct11 4 w=100;
CHANNEL c22 from ct11 2 to ct12 4 w=100;

CHANNEL c23 from ct9 3 to ct13 1 w=100;
CHANNEL c24 from ct10 3 to ct14 1 w=100;
CHANNEL c25 from ct11 3 to ct15 1 w=100;
CHANNEL c26 from ct12 3 to ct16 1 w=100;

CHANNEL c27 from ct13 2 to ct14 4 w=100;
CHANNEL c28 from ct14 2 to ct15 4 w=100;
CHANNEL c29 from ct15 2 to ct16 4 w=100;

CHANNEL c30 from ct13 3 to m2 1 w=100;
CHANNEL c31 from ct14 3 to m2 2 w=100;
CHANNEL c32 from ct15 3 to m2 3 w=100;
CHANNEL c33 from ct16 3 to m2 4 w=100;

CHANNEL c34 from m2 5 to p2 1 w=100;

END LAYER

LAYER CONTROL
V BANK cpb1 of 4 PORT r=100 dir=RIGHT spacing=1500 channelWidth=100;
V BANK cpb2 of 3 PORT r=100 dir=LEFT spacing=1500 channelWidth=100;

VALVE v1 on c6 w=100 l=300;
VALVE v2 on c7 w=100 l=300;
VALVE v3 on c8 w=100 l=300;

VALVE v4 on c9 w=300 l=100;
VALVE v5 on c10 w=300 l=100;
VALVE v6 on c11 w=300 l=100;
VALVE v7 on c12 w=300 l=100;

VALVE v8 on c13 w=100 l=300;
VALVE v9 on c14 w=100 l=300;
VALVE v10 on c15 w=100 l=300;

VALVE v11 on c16 w=300 l=100;
VALVE v12 on c17 w=300 l=100;
VALVE v13 on c18 w=300 l=100;
VALVE v14 on c19 w=300 l=100;

VALVE v15 on c20 w=100 l=300;
VALVE v16 on c21 w=100 l=300;
VALVE v17 on c22 w=100 l=300;

VALVE v18 on c23 w=300 l=100;
VALVE v19 on c24 w=300 l=100;
VALVE v20 on c25 w=300 l=100;
VALVE v21 on c26 w=300 l=100;

VALVE v22 on c27 w=100 l=300;
VALVE v23 on c28 w=100 l=300;
VALVE v24 on c29 w=100 l=300;

NET n1 from cpb1 1 to v1 3, v2 3, v3 3 channelWidth=50;

CHANNEL cc1 from v4 2 to v5 4 w=50;
CHANNEL cc2 from v5 2 to v6 4 w=50;
CHANNEL cc3 from v6 2 to v7 4 w=50;
CHANNEL cc4 from v7 2 to cpb2 1 w=50;

NET n2 from cpb1 2 to v8 3, v9 3, v10 3 channelWidth=50;

CHANNEL cc5 from v11 2 to v12 4 w=50;
CHANNEL cc6 from v12 2 to v13 4 w=50;
CHANNEL cc7 from v13 2 to v14 4 w=50;
CHANNEL cc8 from v14 2 to cpb2 2 w=50;

NET n3 from cpb1 3 to v15 3, v16 3, v17 3 channelWidth=50;

CHANNEL cc9 from v18 2 to v19 4 w=50;
CHANNEL cc10 from v19 2 to v20 4 w=50;
CHANNEL cc11 from v20 2 to v21 4 w=50;
CHANNEL cc12 from v21 2 to cpb2 3 w=50;

NET n4 from cpb1 4 to v22 3, v23 3, v24 3 channelWidth=50;

END LAYER
