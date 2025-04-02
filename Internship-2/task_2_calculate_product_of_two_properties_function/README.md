### **Task 2: Helper Function to Compute Product of Two Properties**

#### **Overview**
This task introduces a helper function, `property-product`, that takes two sets of properties and calculates the product of corresponding property values.

#### **Code**

```MeTTa
(= (property-product $properties1 $properties2)
    (let*(
        ($property1 (car-atom $properties1))
        ($property2 (car-atom $properties2))
        ($num1 (get-num $property1))
        ($num2 (get-num $property2))
        ($num-properties (size-atom $properties1))
        ($product ((car-atom $property1) (* $num1 $num2)))
    )
        (if (not (== $num-properties 1))
            (let*(
                ($tail-properties1 (cdr-atom $properties1))
                ($tail-properties2 (cdr-atom $properties2))
                ($call-back (property-product $tail-properties1 $tail-properties2))
            )
                (cons-atom $product $call-back)
            )
            ($product)
        )
    )
)

; Example Usage:
! (property-product ((web-creation 0.1) (intelligence 0.2) (physical-strength 0.6) (mobility 0.8)
                     (predatory-behavior 1.0) (social-structure 0.2) (symbolism 0.7) (tool-use 0.1))
                    ((web-creation 1.0) (intelligence 0.4) (physical-strength 0.1) (mobility 0.8)
                     (predatory-behavior 1.0) (social-structure 0.2) (symbolism 0.7) (tool-use 0.1)))

; Expected Output:
; [((web-creation 0.1) (intelligence 0.08000000000000002) (physical-strength 0.06)
;   (mobility 0.6400000000000001) (predatory-behavior 1.0) (social-structure 0.04000000000000001)
;   (symbolism 0.48999999999999994) (tool-use 0.010000000000000002))]
```
---
### **Key Features**
- **Efficient Recursive Processing** – Processes each property pair recursively.
- **Preserves Property Order** – Ensures original ordering is maintained in results.

---

#### **Related Links**
- [Commit Reference](https://github.com/iCog-Labs-Dev/conceptBlending/commit/0009e19eccb3f9b3822aed5d1003955b7fcd8f6f)
- [Main Codebase](https://github.com/iCog-Labs-Dev/conceptBlending/)
