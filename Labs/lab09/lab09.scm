; (define (over-or-under num1 num2) 
;   (if (< num1 num2) -1 
;   (if (= num1 num2) 0 1))
; )

(define (over-or-under num1 num2) ; Cond
  (cond ((< num1 num2) -1)
        ((= num1 num2) 0)
        (else 1)
  )
)

(define (make-adder num) 
  (lambda (inc) (+ num inc))
)

(define (composed f g) 
  (lambda (x) (f (g x)))
)

; (define (repeat f n) 
;   (cond ((= n 1) (lambda (x) (f x)))
;     (else (composed f (repeat f (- n 1))))
;   )
; )

(define (repeat f n)
  (if (= n 1) (lambda (x) (f x)) (composed f (repeat f (- n 1)))) ; In one line
)

(define (max a b)
  (if (> a b)
      a
      b))

(define (min a b)
  (if (> a b)
      b
      a))

; (define (gcd a b) 
;   (if (> a b)
;     (if (not (= 0 (modulo a b)))
;       (gcd b (modulo a b))
;       b)
;     (if (= a b)
;     a
;     (gcd b a)
;     )
;   )
; )

; Altering method using max and min
(define (gcd a b)
  (if (not (= 0 (modulo (max a b) (min a b))))
    (gcd (max a b) (modulo (max a b) (min a b)))
    b)
)

(define (duplicate lst) 
    
  (if (null? lst)
    nil
    (cons (car lst) (cons (car lst) (duplicate (cdr lst))))
  )
)

(expect (duplicate '(1 2 3)) (1 1 2 2 3 3))

(expect (duplicate '(1 1)) (1 1 1 1))

(define (deep-map fn s) 
  (
    if (null? s)
      nil
      (
        if (not (list? (car s)))
          (cons (fn (car s)) (deep-map fn (cdr s)))
          (
            if (null? (cdr s))
              (list (deep-map fn (car s)))
              (cons (deep-map fn (car s)) (deep-map fn (cdr s)))
          )
      )
  )
)
