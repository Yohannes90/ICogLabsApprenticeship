### Task 5: calculate Mu-Emergence Function Implementation

#### Overview
This feature adds a `mu-emergence` function that calculates the emergence value for various properties of concepts. It takes two arguments: `property-degree` and `properties-max`. The function destructures `properties-max` to compute a new value for each property based on the difference between `property-degree` and the associated values in `properties-max`.

#### Formula

The formula used for the `mu-emergence` function can be described as:

![Mu-emergence Formula](./task_5_mu-emergence%20formula.png)


#### Code

```MeTTa
(= (mu-emergence $property-degree $properties-max)
    (let*(
        ($property (car-atom $properties-max))
        ($num (get-num $property))
        ($num-properties (size-atom $properties-max))
        ($property-minus-num (- $property-degree $num))
        ($non-zero (max-atom ($property-minus-num 0)))
        ($result ((car-atom $property) $non-zero))
    )
        (if (not (== $num-properties 1))
            (let*(
                ($tail-properties (cdr-atom $properties-max))
                ($call-back (mu-emergence $property-degree $tail-properties))
            )
                (cons-atom $result $call-back)
            )
            ($result)
        )
    )
)


; Example Usage
! (let*(
        ($concept1 (Concept Spider@Man (Property (web-creation 0.1) (intelligence 0.3) (physical-strength 0.6) (mobility 0.8) (predatory-behavior 1.0) (social-structure 0.2) (symbolism 0.7) (tool-use 0.1))))
        ($concept2 (Concept Spider@Man (Property (web-creation 1.0) (intelligence 0.4) (physical-strength 0.2) (mobility 0.8) (predatory-behavior 1.0) (social-structure 0.2) (symbolism 0.7) (tool-use 0.1))))
        ($degree (property-degree $concept1))
        ($max (property-max $concept1 $concept2))
        ($calculated-mu-emergence (mu-emergence $degree $max))
    )
    $calculated-mu-emergence
)

; Expected Output:
; [((web-creation 0.0) (intelligence 0.5030899869919434) (physical-strength 0.30308998699194345) (mobility 0.10308998699194338) (predatory-behavior 0.0) (social-structure 0.7030899869919434) (symbolism 0.20308998699194347) (tool-use 0.8030899869919434))]
```

#### Related Links
- [Commit Reference](https://github.com/iCog-Labs-Dev/conceptBlending/commit/a06885164c5d38f7213673abd553e2068d457e50)
- [Main Codebase](https://github.com/iCog-Labs-Dev/conceptBlending/)
