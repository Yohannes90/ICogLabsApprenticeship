### **Task 3: Refactored `property-degree` Function**

#### **Overview**
This update refactors the `property-degree` function to improve efficiency by making it **more than three times shorter**, showing **clear calculation steps**, and removing **redundant code**. The function calculates the degree of a given **Concept** based on the number of properties it has.

---

### **Previous Code (Before Refactoring)**

```MeTTa
(: concept Concept)
(: get-number-of-properties (-> Concept Number))
(=(get-number-of-properties $concept)
    (
        let*(
                ($a $concept)
                ($b (superpose $a))
        )
    (if (== (get-metatype $b) Expression)
        (let $c (cdr-atom $b)
            (size-atom $c))
        (empty)
    )
        )
    )

;;!(get-number-of-properties (Concept Spider@Man (Property (web-creation 1.0) (intelligence 0.4) (physical-strength 0.6) (mobility 0.8) (predatory-behavior 1.0) (social-structure 0.2) (symbolism 0.7) (tool-use 0.1))))
;;retruns 8


(: property-probability (-> Concept Number))
(=(property-probability $concept)
    (let*(
        ($numberofprops (get-number-of-properties $concept))
        ($probability (/ 1.0 $numberofprops))
    )
    $probability
    )
    )

;;!(property-probability (Concept Spider@Man (Property (web-creation 1.0) (intelligence 0.4) (physical-strength 0.6) (mobility 0.8) (predatory-behavior 1.0) (social-structure 0.2) (symbolism 0.7) (tool-use 0.1))))
;;returns 0.125


(: property-degree (-> Concept Number))
(=(property-degree $concept)
    (let*(
        ($probability (property-probability $concept))
        ($degree (* -1 (log-math 10 $probability)))
    )
    $degree
    )
    )


! (property-degree (Concept Spider@Man (Property (web-creation 1.0) (intelligence 0.4) (physical-strength 0.6) (mobility 0.8) (predatory-behavior 1.0) (social-structure 0.2) (symbolism 0.7) (tool-use 0.1))))
;;returns 0.9030899869919434
```
---

### **Refactored Code (After Optimization)**

```MeTTa
; ###################### Calculate Degree function ##########################
(=(property-degree $concept)
    (let*(
        ($properties (get-properties $concept))
        ($num-properties (size-atom $properties))
        ($probability (/ 1.0 $num-properties))
        ($degree (* -1 (log-math 10 $probability)))
    )
        $degree
    )
)

; Example Usage:
! (property-degree (Concept Spider@Man (Property (web-creation 1.0) (intelligence 0.4) (physical-strength 0.6) (mobility 0.8)
                                         (predatory-behavior 1.0) (social-structure 0.2) (symbolism 0.7) (tool-use 0.1))))

; Expected Output:
; [0.9030899869919434]
```

### **Related Links**
- [Commit Reference](https://github.com/iCog-Labs-Dev/conceptBlending/commit/f490bf34482f0cb47cbde3b3d467d3f63d899ae1)
- [Main Codebase](https://github.com/iCog-Labs-Dev/conceptBlending/)
