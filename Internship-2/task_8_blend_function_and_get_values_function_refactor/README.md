### **Task 8: Blend Function and Utility Refactor**

#### **Overview**

##### Feature: `blend` Function
A new high-level `blend` function has been implemented to generate a conceptual blend between two input concepts. It checks if the `mu-hqblend` score is greater than `0` before proceeding to generate a conceptual network using the `gpt_network_selector`.

##### Refactor: `get-values` Simplification
The existing `get-values` function was refactored to use the built-in `map-atom` function, making the code cleaner, shorter, and eliminates recursion in favor of functional mapping.


#### **Code**

##### **`blend`**

```MeTTa
(= (blend $input1 $input2)
    (let*(
        ($concepts (gpt_vector $input1 $input2))
        ($concept1 (car-atom $concepts))
        ($wrapped-concept2 (cdr-atom $concepts))
        ($concept2 (car-atom $wrapped-concept2))
        ($degree (property-degree $concept1))
        ($max (property-max $concept1 $concept2))
        ($calculated-mu-emergence (mu-emergence $degree $max))
        ($min (property-min $concept1 $concept2))
        ($calculated-mu-hqblend (mu-hqblend $calculated-mu-emergence $min))
        ($unwrapped-concepts (cdr-atom $concept1))
        ($concept-pair (car-atom $unwrapped-concepts))
    )
        (if (> $calculated-mu-hqblend 0)
            (let*(
                ($network (gpt_network_selector $concept-pair))
            )
                (if (not (noreduce-eq $network None))
                    ($network $concept-pair $calculated-mu-emergence)
                    (empty)
                )
            )
            (empty)
        )
    )
)



; Example Usage:
! (blend "Bat" "Man")

; Expected Output:
; [(doubleScope (expand Bat Man) BatMan (extended NocturnalSymbolicHero))]
```

---

#### **Previous Code (Before Refactoring)**

```MeTTa
(=(get-values $properties)
    (let*(
        ($property (car-atom $properties))
        ($num (get-value $property))
        ($num-properties (size-atom $properties))
    )
        (if (not (== $num-properties 1))
            (let*(
                ($tail-properties (cdr-atom $properties))
                ($call-back (get-values $tail-properties))
            )
                (cons-atom $num $call-back)
            )
            ($num)
        )
    )
)

; Example Usage:
! (get-values (get-properties (Concept Spider@Man (Property (web-creation 1.0) (intelligence 0.4) (physical-strength 0.6) (mobility 0.8) (predatory-behavior 1.0) (social-structure 0.2) (symbolism 0.7) (tool-use 0.1)))))

; Expected Output:
; [(1.0 0.4 0.6 0.8 1.0 0.2 0.7 0.1)]
```

#### **Refactored Code (After Optimization)**

```MeTTa
(= (get-values $properties)
    (map-atom $properties $property (get-value $property))
)


(=(get-values $properties)
    (let*(
        ($property (car-atom $properties))
        ($num (get-num $property))
        ($num-properties (size-atom $properties))
    )
        (if (not (== $num-properties 1))
            (let*(
                ($tail-properties (cdr-atom $properties))
                ($call-back (get-values $tail-properties))
            )
                (cons-atom $num $call-back)
            )
            ($num)
        )
    )
)

; Example Usage:
! (get-values (get-properties (Concept Spider@Man (Property (web-creation 1.0) (intelligence 0.4) (physical-strength 0.6) (mobility 0.8) (predatory-behavior 1.0) (social-structure 0.2) (symbolism 0.7) (tool-use 0.1)))))

; Expected Output:
; [(1.0 0.4 0.6 0.8 1.0 0.2 0.7 0.1)]
```

### **Related Links**
- [Commit Reference](https://github.com/iCog-Labs-Dev/conceptBlending/commit/8193aebf1d5f137d895a0faebd43d187022b156a)
- [Commit Reference](https://github.com/iCog-Labs-Dev/conceptBlending/pull/10/commits/fe8af3ba3adbfae54c4ae0c5f50886361f7a9147)
- [Pull Request Reference](https://github.com/iCog-Labs-Dev/conceptBlending/pull/10)
- [Main Codebase](https://github.com/iCog-Labs-Dev/conceptBlending/)
