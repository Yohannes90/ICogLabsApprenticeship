
; Cons type declaration
(: List Type)
(: Nil List)
(: Cons (-> Number List List))

! (get-type (Cons 3 Nil)) ; [List]


; helper functions
; to store sample list
(: myList (-> List))
(= (myList)
    (Cons 42 (Cons 75 (Cons 32 (Cons 23 (Cons 432 (Cons 35 (Cons 94 (Cons 16 (Cons 23 Nil)))))))))
)
! (myList) ; [(Cons 42 (Cons 75 (Cons 32 (Cons 23 (Cons 432 (Cons 35 (Cons 94 (Cons 16 (Cons 23 Nil)))))))))]


; to print list
(= (show Nil) ())
(= (show (Cons $x $xs))
    ($x (show $xs))
)
! (show (myList)) ; [(42 (75 (32 (23 (432 (35 (94 (16 ()))))))))]


; to get first values of list
(: first_value (-> List Number))
(= (first_value (Cons $x $xs)) $x)
! (first_value (myList)) ; [42]


; to add 2, for testing high order functions that take function as a parameter
(: add2 (-> Number Number))
(= (add2 $x) (+ $x 2))

(: lessThan40 (-> Number Bool))
(= (lessThan40 $x) (< $x 40))


; Answers
; 1. length
(: length (-> List Number))
(= (length Nil) 0)
(= (length (Cons $x $xs))
    (+ 1 (length $xs))
)
! (length(myList)) ; [9]


; 2. is-member
(: is_member (-> Number List Bool))
(= (is_member $y Nil) False)
(= (is_member $y (Cons $x $xs))
    (if (== $y $x)
        True
    (is_member $y $xs))
)
! (is_member 432 (myList)) ; [True]
! (is_member 4322 (myList)) ; [False]


; 3. append
(: append (-> Number List List))
(= (append $y Nil) (Cons $y Nil))
(= (append $y (Cons $x $xs))
    (Cons $x (append $y $xs)))
! (append 332 (myList)) ; [(Cons 42 (Cons 75 (Cons 32 (Cons 23 (Cons 432 (Cons 35 (Cons 94 (Cons 16 (Cons 23 (Cons 332 Nil))))))))))]


; 4. max-value
; 5. min-value


; 6. push - adding to the begining of the list
(: push (-> Number List List))
(= (push $x $list) (Cons $x $list))
! (push 43 (myList)) ; [(Cons 43 (Cons 42 (Cons 75 (Cons 32 (Cons 23 (Cons 432 (Cons 35 (Cons 94 (Cons 16 (Cons 23 Nil))))))))))]


; 7. pop removing from the begining of the list
(: pop (-> List List))
(= (pop (Cons $x $xs)) $xs)
! (pop (myList)) ; [(Cons 75 (Cons 32 (Cons 23 (Cons 432 (Cons 35 (Cons 94 (Cons 16 (Cons 23 Nil))))))))]


; 8. remove-element
(: remove (-> Number List List))
(= (remove $y ()) ())
(= (remove $y Nil) Nil)
(= (remove $y (Cons $x $xs))
    (if (== $y $x)
        (remove $y $xs)
        (Cons $x (remove $y $xs))
    )
)
! (remove 32 (myList)) ; [(Cons 42 (Cons 75 (Cons 23 (Cons 432 (Cons 35 (Cons 94 (Cons 16 (Cons 23 Nil))))))))]


; 9. remove-duplicate


; 10. map
(: map (-> (-> Number Number) List List))
(= (map $func ()) ())
(= (map $func Nil) Nil)
(= (map $func (Cons $x $xs))
    (Cons ($func $x) (map $func $xs))
)
! (show (myList)) ; [(42 (75 (32 (23 (432 (35 (94 (16 (23 ())))))))))]
! (map add2 (myList)) ; [(Cons 44 (Cons 77 (Cons 34 (Cons 25 (Cons 434 (Cons 37 (Cons 96 (Cons 18 (Cons 25 Nil)))))))))]


; 11. filter
(: filter (-> (-> Number Bool) List List))
(= (filter $func ()) ())
(= (filter $func Nil) Nil)
(= (filter $func (Cons $x $xs))
    (if ($func $x)
        (Cons $x (filter $func $xs))
    (filter $func $xs)
    )
)
! (show (myList)) ; [(42 (75 (32 (23 (432 (35 (94 (16 (23 ())))))))))]
! (filter lessThan40 (myList)) ; [(Cons 32 (Cons 23 (Cons 35 (Cons 16 (Cons 23 Nil)))))]


; 12. foldl
; 13. foldr
; 14. reverse
; 15. sort
