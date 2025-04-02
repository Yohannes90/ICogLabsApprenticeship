### **Task 4: Adding `max-property`, `min-property`, `property-min` and `property-max` Functions**

#### **Overview**
This update introduces two key functionalities to compare properties between concepts: `min-property` and `max-property`. These functions compute the minimum and maximum values for each property across two lists, providing a simple way to compare two concepts. Additionally, the `property-min` and `property-max` functions wrap these operations to apply them at the concept level.

#### **Code**

##### **`min-property`**

This function recursively compares two lists of properties and returns a new list with the minimum values for each property across the two inputs.

```MeTTa
(= (min-property $properties1 $properties2)
    (let*(
        ($property1 (car-atom $properties1))
        ($property2 (car-atom $properties2))
        ($num1 (get-num $property1))
        ($num2 (get-num $property2))
        ($num-properties (size-atom $properties1))
        ($min-prop ((car-atom $property1) (min-atom ($num1 $num2))))
    )
        (if (not (== $num-properties 1))
            (let*(
                ($tail-properties1 (cdr-atom $properties1))
                ($tail-properties2 (cdr-atom $properties2))
                ($call-back (min-property $tail-properties1 $tail-properties2))
            )
                (cons-atom $min-prop $call-back)
            )
            ($min-prop)
        )
    )
)

; Example Usage:
! (min-property ((web-creation 0.1) (intelligence 0.2) (physical-strength 0.6) (mobility 0.8)
                 (predatory-behavior 1.0) (social-structure 0.2) (symbolism 0.7) (tool-use 0.1))
                ((web-creation 1.0) (intelligence 0.4) (physical-strength 0.1) (mobility 0.8)
                 (predatory-behavior 1.0) (social-structure 0.2) (symbolism 0.7) (tool-use 0.1)))

; Expected Output:
; [((web-creation 0.1) (intelligence 0.2) (physical-strength 0.1) (mobility 0.8)
;   (predatory-behavior 1.0) (social-structure 0.2) (symbolism 0.7) (tool-use 0.1))]

```


##### **`max-property`**

This function recursively compares two lists of properties and returns a new list with the maximum values for each property across the two inputs.

```MeTTa

(= (max-property $properties1 $properties2)
    (let*(
        ($property1 (car-atom $properties1))
        ($property2 (car-atom $properties2))
        ($num1 (get-num $property1))
        ($num2 (get-num $property2))
        ($num-properties (size-atom $properties1))
        ($max-prop ((car-atom $property1) (max-atom ($num1 $num2))))
    )
        (if (not (== $num-properties 1))
            (let*(
                ($tail-properties1 (cdr-atom $properties1))
                ($tail-properties2 (cdr-atom $properties2))
                ($call-back (max-property $tail-properties1 $tail-properties2))
            )
                (cons-atom $max-prop $call-back)
            )
            ($max-prop)
        )
    )
)

; Example Usage:
! (max-property ((web-creation 0.1) (intelligence 0.2) (physical-strength 0.6) (mobility 0.8)
                 (predatory-behavior 1.0) (social-structure 0.2) (symbolism 0.7) (tool-use 0.1))
                ((web-creation 1.0) (intelligence 0.4) (physical-strength 0.1) (mobility 0.8)
                 (predatory-behavior 1.0) (social-structure 0.2) (symbolism 0.7) (tool-use 0.1)))

; Expected Output:
; [((web-creation 1.0) (intelligence 0.4) (physical-strength 0.6) (mobility 0.8)
;   (predatory-behavior 1.0) (social-structure 0.2) (symbolism 0.7) (tool-use 0.1))]
```

---

##### **`property-min` and `property-max`**

These wrapper functions compare the properties of two concepts. They extract the property lists of the concepts using `get-properties` and then call `min-property` or `max-property` to compute the minimum or maximum values.

###### **`property-min` Function:**
```MeTTa
(=(property-min $concept1 $concept2)
    (let*(
        ($properties1 (get-properties $concept1)) ; Extract properties of the first concept
        ($properties2 (get-properties $concept2)) ; Extract properties of the second concept
    )
        ; Call min-property function to compute minimum for each property
        (min-property $properties1 $properties2)
    )
)

; Example Usage:
! (property-min (Concept Spider@Man (Property (web-creation 0.1) (intelligence 0.3) (physical-strength 0.6) (mobility 0.8)
                                       (predatory-behavior 1.0) (social-structure 0.2) (symbolism 0.7) (tool-use 0.1)))
                (Concept Spider@Man (Property (web-creation 1.0) (intelligence 0.4) (physical-strength 0.2) (mobility 0.8)
                                       (predatory-behavior 1.0) (social-structure 0.2) (symbolism 0.7) (tool-use 0.1))))

; Expected Output:
; [((web-creation 0.1) (intelligence 0.3) (physical-strength 0.2) (mobility 0.8)
;   (predatory-behavior 1.0) (social-structure 0.2) (symbolism 0.7) (tool-use 0.1))]
```

###### **`property-max` Function:**
```MeTTa
(=(property-max $concept1 $concept2)
    (let*(
        ($properties1 (get-properties $concept1)) ; Extract properties of the first concept
        ($properties2 (get-properties $concept2)) ; Extract properties of the second concept
    )
        ; Call max-property function to compute maximum for each property
        (max-property $properties1 $properties2)
    )
)

; Example Usage:
! (property-max (Concept Spider@Man (Property (web-creation 0.1) (intelligence 0.3) (physical-strength 0.6) (mobility 0.8)
                                       (predatory-behavior 1.0) (social-structure 0.2) (symbolism 0.7) (tool-use 0.1)))
                (Concept Spider@Man (Property (web-creation 1.0) (intelligence 0.4) (physical-strength 0.2) (mobility 0.8)
                                       (predatory-behavior 1.0) (social-structure 0.2) (symbolism 0.7) (tool-use 0.1))))

; Expected Output:
; [((web-creation 1.0) (intelligence 0.4) (physical-strength 0.6) (mobility 0.8)
;   (predatory-behavior 1.0) (social-structure 0.2) (symbolism 0.7) (tool-use 0.1))]
```
---

### **Key Features**
- **Efficient Recursive Processing** – The min/max functions process each property pair recursively, ensuring scalability for lists of any length.
- **Accurate Min/Max Extraction** – By using `min-atom` and `max-atom`, the values are correctly compared, guaranteeing accurate results.
- **Preserved Property Order** – The original order of properties in the results is maintained, making the output intuitive and usable.


### **Related Links**
- [Commit Reference](https://github.com/iCog-Labs-Dev/conceptBlending/commit/74977708d34a665e5c61851bfc00d06b69a1b09c)
- [Commit Reference](https://github.com/iCog-Labs-Dev/conceptBlending/commit/39aa5676951652d838ea151f57f22c5a005ce07b)
- [Main Codebase](https://github.com/iCog-Labs-Dev/conceptBlending/)
