grammar mus;

expr: left=expr op=('+'|'-') right=expr        # InfixExpr
    | '(' expr ')'                             # ParenExpr 
    | atom=INT                                 # NumberExpr
    | atom=REAL                                # RealExpr
    | atom=NOTA                                # NotaExpr
    | atom=CHORD                               # ChordExpr
    | atom=STAVE                               # StaveExpr
    | atom=SONGS                               # SongsExpr
    | atom=LIST                                # ListExpr
    | atom=HELLO                               # HelloExpr
    | atom=BYE                                 # ByeExpr
    ;

fragment WORD : [A-Za-z][A-Za-z0-9]*;

INT  : [0-9]+          ;
REAL : INT'.'INT       ;
NOTA : [a-g][0-9] 
     | [a-g]'#'[0-9]   ;
CHORD: [A-G]
     | [A-G]'m'
     | [A-G]'#' 
     | [A-G]'#''m'     ;

WS   : [ \t]+ -> skip  ;

FIRST_STAVE_ELEMENT : NOTA | CHORD;
fragment STAVE_ELEMENT : (WS* '_' WS* FIRST_STAVE_ELEMENT )*;
STAVE : '~' WS* FIRST_STAVE_ELEMENT STAVE_ELEMENT WS* '~';

FIRST_SONG : WORD WS* '=>' WS* STAVE;
fragment SONG : (WS* ',' WS* FIRST_SONG )*;
SONGS : '{' WS* FIRST_SONG SONG WS* '}';

FIRST_LIST_ELEMENT : INT | REAL | NOTA | CHORD | STAVE | SONGS;
fragment LIST_ELEMENT : (WS* ',' WS* FIRST_LIST_ELEMENT )*;
LIST : '[' WS* FIRST_LIST_ELEMENT LIST_ELEMENT WS* ']';

HELLO: ('hello'|'hi'|'hallo'|'privet'|'whoami'|'SAYMYNAME!');
BYE  : ('bye'|'tata'|'yougoddamnright');
