.integer 2 1
.mult 2 10
.add 2 4
.div 1 40
LD    F6,   34(R2)
LD    F2,   45(R3)
MULTD F0,   F2, F4
MULTD F6,   F2, F4
SUBD  F8,   F6, F2
ADDD  F0,   F8, F2
DIVD  F10,  F0, F6
ADDD  F6,   F8, F2
