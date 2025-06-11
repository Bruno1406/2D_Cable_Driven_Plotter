grammar Gcode;

gcode: statement+ programEnd;

statement
    : lineNumber codFunc coord* lineEnd
    ;

programEnd
    : lineNumber mEnd
    ;

lineNumber
    : 'N' INT
    ;

codFunc
    : 'G' INT
    ;

mEnd
    : 'M30'
    ;

coord
    : coordX
    | coordY
    | coordI
    | coordJ 
    ;

coordX
    : 'X' coordValue
    ;

coordY
    : 'Y' coordValue
    ;

coordI
    : 'I' coordValue
    ;

coordJ
    : 'J' coordValue
    ;

coordValue
    : signedInt ('.' INT)?     // allows 100, 100.5, etc.
    ;

lineEnd
    : '\n'
    ;

SIGN : '+' | '-';
INT : [0-9]+;
signedInt : SIGN? INT;
WS : [ \t\r]+ -> skip;