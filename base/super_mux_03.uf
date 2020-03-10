DEVICE super_mux_03

LAYER FLOW
V BANK b1 of 8 PORT r=100 dir=RIGHT spacing=1500 channelWidth=100;
V BANK b2 of 8 CELL TRAP numChambers=10 chamberWidth=100 chamberLength=100 chamberSpacing=30 spacing=1500 channelWidth=100;
V TREE m1 8 to 1 spacing=1500 flowChannelWidth=100;
H MUX m2 2 to 1 spacing=1500 flowChannelWidth=100 controlChannelWidth=20;
H BANK b3 of 2 PORT r=100 dir=DOWN spacing=1500 channelWidth=100;
PORT p1, p2 r=100;
NODE n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12, n13, n14, n15, n16;

CHANNEL c1 from b1 1 to n1 4 w=100;
CHANNEL c2 from b1 2 to n2 4 w=100;
CHANNEL c3 from b1 3 to n3 4 w=100;
CHANNEL c4 from b1 4 to n4 4 w=100;
CHANNEL c5 from b1 5 to n5 4 w=100;
CHANNEL c6 from b1 6 to n6 4 w=100;
CHANNEL c7 from b1 7 to n7 4 w=100;
CHANNEL c8 from b1 8 to n8 4 w=100;

CHANNEL c9 from n1 3 to n2 1 w=100;
CHANNEL c10 from n2 3 to n3 1 w=100;
CHANNEL c11 from n3 3 to n4 1 w=100;
CHANNEL c12 from n4 3 to n5 1 w=100;
CHANNEL c13 from n5 3 to n6 1 w=100;
CHANNEL c14 from n6 3 to n7 1 w=100;
CHANNEL c15 from n7 3 to n8 1 w=100;

CHANNEL c16 from n1 2 to b2 1 w=100;
CHANNEL c17 from n2 2 to b2 2 w=100;
CHANNEL c18 from n3 2 to b2 3 w=100;
CHANNEL c19 from n4 2 to b2 4 w=100;
CHANNEL c20 from n5 2 to b2 5 w=100;
CHANNEL c21 from n6 2 to b2 6 w=100;
CHANNEL c22 from n7 2 to b2 7 w=100;
CHANNEL c23 from n8 2 to b2 8 w=100;

CHANNEL c24 from b2 9 to n9 4 w=100;
CHANNEL c25 from b2 10 to n10 4 w=100;
CHANNEL c26 from b2 11 to n11 4 w=100;
CHANNEL c27 from b2 12 to n12 4 w=100;
CHANNEL c28 from b2 13 to n13 4 w=100;
CHANNEL c29 from b2 14 to n14 4 w=100;
CHANNEL c30 from b2 15 to n15 4 w=100;
CHANNEL c31 from b2 16 to n16 4 w=100;

CHANNEL c32 from n9 3 to n10 1 w=100;
CHANNEL c33 from n10 3 to n11 1 w=100;
CHANNEL c34 from n11 3 to n12 1 w=100;
CHANNEL c35 from n12 3 to n13 1 w=100;
CHANNEL c36 from n13 3 to n14 1 w=100;
CHANNEL c37 from n14 3 to n15 1 w=100;
CHANNEL c38 from n15 3 to n16 1 w=100;
CHANNEL c39 from n16 3 to p1 1 w=100;

CHANNEL c40 from n9 2 to m1 1 w=100;
CHANNEL c41 from n10 2 to m1 2 w=100;
CHANNEL c42 from n11 2 to m1 3 w=100;
CHANNEL c43 from n12 2 to m1 4 w=100;
CHANNEL c44 from n13 2 to m1 5 w=100;
CHANNEL c45 from n14 2 to m1 6 w=100;
CHANNEL c46 from n15 2 to m1 7 w=100;
CHANNEL c47 from n16 2 to m1 8 w=100;

CHANNEL c48 from m1 9 to p2 4 w=100;

CHANNEL c49 from n1 1 to m2 3 w=100;
CHANNEL c50 from b3 1 to m2 1 w=100;
CHANNEL c51 from b3 2 to m2 2 w=100;

END LAYER

LAYER CONTROL

PORT cp1, cp2 r=100;

CHANNEL cx1 from cp1 2 to m2 4 w=20;
CHANNEL cx2 from cp2 4 to m2 5 w=20;

END LAYER

