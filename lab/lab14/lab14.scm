(define (split-at lst n)
  (cond
    ((null? lst) (cons nil nil))
    ((= n 0) (cons nil lst))
    (else
      (cons (cons (car lst) (car (split-at (cdr lst) (- n 1))))
        (cdr (split-at (cdr lst) (- n 1)))
        )
      )
    )
  )

(define (compose-all funcs)
  ( define (abc x funcs)
    (cond
      ((null? funcs) x)
      (else (abc (lambda (y) ((car funcs) (x y)) ) (cdr funcs)))
      )
    )
  (abc (lambda (x) x) funcs)
  )
