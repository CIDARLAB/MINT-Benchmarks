DEVICE hmux01

LAYER FLOW
H MUX m1 1 to 8 spacing=1000 flowChannelWidth=100 controlChannelWidth=20;
PORT p1 r=200;

H BANK pb of 8 PORT r=100 dir=UP spacing=1000 channelWidth=100;

CHANNEL c1 from p1 3 to m1 1 w=100;

CHANNEL c1 from pb 1 to m1 2 w=100;
CHANNEL c1 from pb 2 to m1 3 w=100;
CHANNEL c1 from pb 3 to m1 4 w=100;
CHANNEL c1 from pb 4 to m1 5 w=100;
CHANNEL c1 from pb 5 to m1 6 w=100;
CHANNEL c1 from pb 6 to m1 7 w=100;
CHANNEL c1 from pb 7 to m1 8 w=100;
CHANNEL c1 from pb 8 to m1 9 w=100;

END LAYER

LAYER CONTROL

PORT cp1, cp2, cp3, cp4, cp5, cp6 r=200;

CHANNEL cc1 from cp1 4 to m1 10 w=20;
CHANNEL cc2 from cp2 4 to m1 12 w=20;
CHANNEL cc3 from cp3 4 to m1 14 w=20;
CHANNEL cc4 from cp4 2 to m1 11 w=20;
CHANNEL cc5 from cp5 2 to m1 13 w=20;
CHANNEL cc6 from cp6 2 to m1 15 w=20;

END LAYER


