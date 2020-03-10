DEVICE super_mux_01

LAYER FLOW
V TREE m1 8 to 1 spacing=1500 flowChannelWidth=100;
V BANK b2 of 8 CELL TRAP numChambers=10 chamberWidth=100 chamberLength=100 chamberSpacing=30 spacing=1500 channelWidth=100;
V BANK pb of 8 PORT dir=RIGHT r=100 spacing=1500 channelWidth=100;
PORT p1, p2 r=100;
NODE n9, n10, n11, n12, n13, n14, n15, n16;

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
CHANNEL c39 from n16 3 to p2 1 w=100;

CHANNEL c40 from n9 2 to m1 1 w=100;
CHANNEL c41 from n10 2 to m1 2 w=100;
CHANNEL c42 from n11 2 to m1 3 w=100;
CHANNEL c43 from n12 2 to m1 4 w=100;
CHANNEL c44 from n13 2 to m1 5 w=100;
CHANNEL c45 from n14 2 to m1 6 w=100;
CHANNEL c46 from n15 2 to m1 7 w=100;
CHANNEL c47 from n16 2 to m1 8 w=100;

CHANNEL c48 from m1 9 to p1 4 w=100;

CHANNEL c50 from b2 1 to pb 1 w=100;
CHANNEL c51 from b2 2 to pb 2 w=100;
CHANNEL c52 from b2 3 to pb 3 w=100;
CHANNEL c53 from b2 4 to pb 4 w=100;

CHANNEL c54 from b2 5 to pb 5 w=100;
CHANNEL c55 from b2 6 to pb 6 w=100;
CHANNEL c56 from b2 7 to pb 7 w=100;
CHANNEL c57 from b2 8 to pb 8 w=100;

END LAYER

LAYER CONTROL
PORT cp5, cp6 r=100;
NODE cn9, cn10, cn11, cn12, cn13, cn14, cn15, cn16;

VALVE v17 on c32 w=200 l=100;
VALVE v18 on c33 w=200 l=100;
VALVE v19 on c34 w=200 l=100;
VALVE v20 on c35 w=200 l=100;
VALVE v21 on c36 w=200 l=100;
VALVE v22 on c37 w=200 l=100;
VALVE v23 on c38 w=200 l=100;
VALVE v24 on c39 w=200 l=100;
CHANNEL cc25 from v17 4 to cn9 2 w=20;
CHANNEL cc26 from v18 4 to cn10 2 w=20;
CHANNEL cc27 from v19 4 to cn11 2 w=20;
CHANNEL cc28 from v20 4 to cn12 2 w=20;
CHANNEL cc29 from v21 4 to cn13 2 w=20;
CHANNEL cc30 from v22 4 to cn14 2 w=20;
CHANNEL cc31 from v23 4 to cn15 2 w=20;
CHANNEL cc32 from v24 4 to cn16 2 w=20;
CHANNEL cc33 from cn9 3 to cn10 1 w=20;
CHANNEL cc34 from cn10 3 to cn11 1 w=20;
CHANNEL cc35 from cn11 3 to cn12 1 w=20;
CHANNEL cc36 from cn12 3 to cn13 1 w=20;
CHANNEL cc37 from cn13 3 to cn14 1 w=20;
CHANNEL cc38 from cn14 3 to cn15 1 w=20;
CHANNEL cc39 from cn15 3 to cn16 1 w=20;
CHANNEL cc40 from cn16 3 to cp5 1 w=20;

VALVE v25 on c40 w=100 l=200;
VALVE v26 on c41 w=100 l=200;
VALVE v27 on c42 w=100 l=200;
VALVE v28 on c43 w=100 l=200;
VALVE v29 on c44 w=100 l=200;
VALVE v30 on c45 w=100 l=200;
VALVE v31 on c46 w=100 l=200;
VALVE v32 on c47 w=100 l=200;
CHANNEL cc41 from v25 3 to v26 1 w=20;
CHANNEL cc42 from v26 3 to v27 1 w=20;
CHANNEL cc43 from v27 3 to v28 1 w=20;
CHANNEL cc44 from v28 3 to v29 1 w=20;
CHANNEL cc45 from v29 3 to v30 1 w=20;
CHANNEL cc46 from v30 3 to v31 1 w=20;
CHANNEL cc47 from v31 3 to v32 1 w=20;
CHANNEL cc48 from v25 1 to cp6 3 w=20;

END LAYER
