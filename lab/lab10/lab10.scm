(define (over-or-under num1 num2)
    (if (> num1 num2)
    1
    (if (< num1 num2)
    -1
    0)))


(define (make-adder num)
    (define (procedure inc) (+ num inc))
    procedure)

(define (composed f g)
    (define (procedure x)(f (g x)))
    procedure
)

(define lst (cons (cons 1 nil) (cons 2 (cons(cons 3 (cons 4 nil)) (cons 5 nil)))))

(define (remove item lst) 'YOUR-CODE-HERE)
