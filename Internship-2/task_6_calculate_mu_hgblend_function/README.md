### Task 6: Mu-HQBlend Function Implementation

#### Overview
This feature adds the `mu-hqblend` function, which calculates a blend value between two concepts based on their properties. It takes two arguments: the calculated `mu-emergence` value and `properties-min`. The function calculates the product of each corresponding property value between `mu-emergence` and `properties-min`, then sums the products. It scales the sum by multiplying by \( \frac{1}{\text{num-properties}} \) and returns the minimum of this result and 1.


#### Formula

The formula used for the `mu-hqblend` function can be described as:

![Mu-HQBlend Formula](./task_6_mu-hq-blend%20formula.png)


#### Code

```MeTTa
(= (mu-hqblend $mu-emer $properties-min)
    (let*(
        ($product-emer-min (property-product $mu-emer $properties-min))
        ($product-emer-min-nums (get-values $product-emer-min))
        ($product-emer-min-summation (foldl-atom $product-emer-min-nums 0 $acc $val (+ $acc $val)))
        ($num-properties (size-atom $product-emer-min))
        ($1-over-prop (/ 1.0 $num-properties))
        ($1-over-prop-summation (* $1-over-prop $product-emer-min-summation))
    )
        (min-atom ($1-over-prop-summation 1))
    )
)


; Example Usage:
! (let*(
        ($concept1 (Concept Spider@Man (Property (web-creation 0.1) (intelligence 0.3) (physical-strength 0.6) (mobility 0.8) (predatory-behavior 1.0) (social-structure 0.2) (symbolism 0.7) (tool-use 0.1))))
        ($concept2 (Concept Spider@Man (Property (web-creation 1.0) (intelligence 0.4) (physical-strength 0.2) (mobility 0.8) (predatory-behavior 1.0) (social-structure 0.2) (symbolism 0.7) (tool-use 0.1))))
        ($degree (property-degree $concept1))
        ($max (property-max $concept1 $concept2))
        ($min (property-min $concept1 $concept2))
        ($calculated-mu-emergence (mu-emergence $degree $max))
        ($calculated-mu-hqblend (mu-hqblend $calculated-mu-emergence $min))
     )
     $calculated-mu-hqblend
)

; Expected Output:
; [0.08213837126018374]

```

#### Related Links
- [Commit Reference](https://github.com/iCog-Labs-Dev/conceptBlending/commit/c13816e525fef1cdd7028a91f17ba77d38145cc3)
- [Main Codebase](https://github.com/iCog-Labs-Dev/conceptBlending/)
