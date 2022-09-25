(define (cddr s) (cdr (cdr s)))

(define (cadr s) (car (cdr s)))

(define (caddr s) (car (cdr (cdr s))))

(define (ordered? s)
  (if (or (null? s) (null? (cdr s)))
    #t
    (and (<= (car s) (cadr s)) (ordered? (cdr s) ) ) ) )

(define (square x) (* x x))

(define (pow base exp)
  (if
    (= 1 exp) base
    (if (even? exp)
      (pow (square base) (/ exp 2))
      (* (pow (square base) (/ (- exp 1) 2))  base )
      )
    )
  )
