#lang racket
;This is a comment
;Do this for multi-line comments

(provide(all-defined-out))

(define s "Hello") ;Defines 's' as a string with value of "Hello"
 
(define add (+ 2 2)) ;Defines 'add' as the sum of 2 and 2
;Calling functions in racket = ("Function" "args") e.g. (+(func)2 2(args))

(define square  ;Defining a new function
  (lambda (x)   ;Setting the arguments (in this case only 'x')
    (* x x)))   ;No need for return statements, defining the function operation

(define cube
  (lambda (x)
    (* x x x))) ;* function takes any number of arguments and returns product