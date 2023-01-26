Module Cols
===========

Classes
-------

`Cols(t)`
:   Factory for creating NUMs and SYMs

    ### Methods

    `add(self, row)`
    :Module Data
===========

Classes
-------

`Data(src={})`
:   Container for ROWs, summarized into NUM or SYM columns

    ### Methods

    `add(self, t)`
    :   Adds rows and columns

    `clone(self, t, data)`
    :   Creates clone

    `stats(self, cols, nPlaces, what='mid')`
    :Module Num
==========

Classes
-------

`Num(at=0, txt='')`
:   Summarize stream of numbers

    ### Methods

    `add(self, n)`
    :

    `div(self)`
    :   Return standard deviation

    `mid(self)`
    :   Returns mean

    `rnd(self, x, n)`
    :Module Row
==========

Classes
-------

`Row(t)`
:   Container for one recordModule Sym
==========

Classes
-------

`Sym(at=0, txt='')`
:   Summarize stream of symbols

    ### Methods

    `add(self, x)`
    :

    `div(self)`
    :   Returns entropy

    `mid(self)`
    :   Returns mode

    `rnd(self, x, n)`
    :Module Tests
============

Functions
---------

    
`count(t)`
:   

    
`eg_check_nums(the)`
:   Tests Num

    
`eg_check_rands(the)`
:   

    
`eg_check_syms(the)`
:   Tests Sym

    
`eg_csv(the)`
:   

    
`eg_data(the)`
:   Tests Data

    
`eg_stats(the)`
:   

    
`eg_the(the)`
: