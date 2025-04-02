### **Task 1: Helper Functions to Extract Properties, Numbers, and Values**

#### **Overview**
This task introduces essential helper functions to destructure a given **Concept** and extract its **properties, numerical values, and associated values**. These functions are foundational for further calculations involving conceptual blending and property manipulations.

#### **Code**

```MeTTa
(=(get-properties $concept)
    (let*(
        ($full-concept (superpose $concept))
    )
        (if (== (get-metatype $full-concept) Expression)
            (let $property (cdr-atom $full-concept)
                $property)
            (empty)
        )
    )
)
; Example Usage:
! (get-properties (Concept Spider@Man (Property (web-creation 1.0) (intelligence 0.4) (physical-strength 0.6) (mobility 0.8) (predatory-behavior 1.0) (social-structure 0.2) (symbolism 0.7) (tool-use 0.1))))
; Expected Output:
; [((web-creation 1.0) (intelligence 0.4) (physical-strength 0.6) (mobility 0.8) (predatory-behavior 1.0) (social-structure 0.2) (symbolism 0.7) (tool-use 0.1))]


(= (get-num $property)
    (let*(
        ($value (cdr-atom $property))
        ($num (car-atom $value))
    )
        $num
    )
)
; Example Usage:
! (get-num (web-creation 1.0))
; Expected Output:
; [1.0]


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

#### **Related Links** (Repo is currently private)
- [Commit Reference](https://github.com/iCog-Labs-Dev/conceptBlending/commit/f05de0cf3bb984603082198fbb9d53ac5faed6dd)
- [Main Codebase](https://github.com/iCog-Labs-Dev/conceptBlending/)
