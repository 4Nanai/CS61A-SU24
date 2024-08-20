(define (square n) (* n n))

(define (pow base exp)
        (
                if (= exp 1)
                        base
                        (
                                if (even? exp)
                                        (pow (square base) (/ exp 2))
                                        (* base (pow base (- exp 1)))
                        )
        )
)

(define (repeatedly-cube n x)
  (if (zero? n)
      x
      (let ((y (repeatedly-cube (- n 1) x)))
        (* y y y))))

(define (cddr s) (cdr (cdr s)))

(define (cadr s) (car (cdr s)))

(define (caddr s) (car (cdr (cdr s))))

(define (ascending? s) 
        (if (null? s)
                #t
                (if (null? (cdr s))
                        #t
                        (if (not (> (car s) (cadr s)))
                                (ascending? (cdr s))
                                #f))
        )
)

(define (my-filter pred s)
        (if (null? s)
                nil
                (if (pred (car s))
                        (cons (car s) (my-filter pred (cdr s)))
                        (my-filter pred (cdr s))
                )
        )
)

(define (no-repeats s) 
        (if (null? s)
                nil
                (cons (car s) (no-repeats (my-filter (lambda (x) (not (= x (car s)))) (cdr s))))
        )
)

; helper function
; returns the values of lst that are bigger than x
; e.g., (larger-values 3 '(1 2 3 4 5 1 2 3 4 5)) --> (4 5 4 5)
(define (larger-values x lst)
  ______________________________________________)

(define (longest-increasing-subsequence lst)
  (if (null? lst)
      nil
      (begin (define first (car lst))
             (define rest (cdr lst))
             (define large-values-rest
                     (larger-values first rest))
             (define with-first
                     ______________________________________________)
             (define without-first
                     ______________________________________________)
             (if ______________________________________________
                 with-first
                 without-first))))
