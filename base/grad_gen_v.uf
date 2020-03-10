DEVICE grad_gen_v

LAYER FLOW
H BANK b of 4 PORT r=100 dir=DOWN spacing=1500 channelWidth=100;
NODE n1, n2, n3, n4, n5;
V GRADIENT GENERATOR g 3 to 7 numBends=5 bendSpacing=100 bendLength=500 channelWidth=100;
PORT p1 r=100;

CHANNEL c1 from b 1 to n1 4 w=100;
CHANNEL c2 from b 2 to n2 1 w=100;
CHANNEL c3 from b 3 to n4 1 w=100;
CHANNEL c4 from b 4 to n5 2 w=100;
CHANNEL c5 from n1 2 to n2 4 w=100;
CHANNEL c6 from n2 2 to n3 4 w=100;
CHANNEL c7 from n3 2 to n4 4 w=100;
CHANNEL c8 from n4 2 to n5 4 w=100;

CHANNEL c9 from n1 3 to g 1 w=100;
CHANNEL c10 from n3 3 to g 2 w=100;
CHANNEL c11 from n5 3 to g 3 w=100;

CHANNEL c12 from g 4 to p1 1 w=100;
END LAYER
