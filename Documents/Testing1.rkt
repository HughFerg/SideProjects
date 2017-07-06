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

(define (cube2 x) ;Can also define args here (probably generally easier)
  (* x x x))

(define (pow1 x y) ; X to the Y power
  (if (= y 0) ;IF STATEMENTS (if-then-else) format so in this case, if y == 0 then return 1, else multiply by x then recursively call function with y - 1
      1
      (* x (pow1 x (- y 1)))))