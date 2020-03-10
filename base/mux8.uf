DEVICE mux8

LAYER FLOW
H BANK b1 of 8 PORT r=100 dir=DOWN spacing=1200 channelWidth=100;
H MUX m0 8 to 1 spacing=1200 flowChannelWidth=100 controlChannelWidth=50;
PORT p1 r=100;
CHANNEL ca from b1 1 to m0 1 w=100;
CHANNEL cb from b1 2 to m0 2 w=100;
CHANNEL cc from b1 3 to m0 3 w=100;
CHANNEL cd from b1 4 to m0 4 w=100;
CHANNEL ce from b1 5 to m0 5 w=100;
CHANNEL cf from b1 6 to m0 6 w=100;
CHANNEL cg from b1 7 to m0 7 w=100;
CHANNEL ch from b1 8 to m0 8 w=100;
CHANNEL c1 from m0 9 to p1 1 w=100;
END LAYER

LAYER CONTROL
V BANK cb3 of 3 PORT r=100 dir=RIGHT spacing=1200 channelWidth=50;
V BANK cb4 of 3 PORT r=100 dir=LEFT spacing=1200 channelWidth=50;
CHANNEL cc57 from m0 10 to cb3 1 w=50;
CHANNEL cc58 from m0 12 to cb3 2 w=50;
CHANNEL cc59 from m0 14 to cb3 3 w=50;
CHANNEL cc60 from m0 11 to cb4 1 w=50;
CHANNEL cc61 from m0 13 to cb4 2 w=50;
CHANNEL cc62 from m0 15 to cb4 3 w=50;
END LAYER