# Task 1. McCulloch/Pitts Networks (2 points)
a) Construct a McCulloch/Pitts network that simulates the NOR function. (1 P.)
b) How is a McCulloch/Pitts neuron defined? (1 P.)

b before a make more sense:

b)
A McCulloch/Pitts neuron is defined as a 5-Tuple:
– Input vector x⃗ = (x1,...,xn) ∈ Rn
– Weight vector w⃗ = (w1,...,w1) ∈ Rn
– Activation function fa: Rn x Rn --> R
– Output function fo: R --> R
– Output o = fo(fa(x⃗,w⃗))

a)
x⃗ = (x1,x2)
w⃗ = (-1,-1)
fa(x,w) := ∑ xi*wi (as per lecture)
fo with T ≥ 0 (1 if fa(x,w) ≥ 0; 0 else)

| x1 | x2 | x1*w1 | x2*w2 | fa | o |
|----|----|-------|-------|----|---|
| 0  | 0  | 0     | 0     | 0  | 1 |
| 0  | 1  | 0     | -1    | -1 | 0 |
| 1  | 0  | -1    | 0     | -1 | 0 |
| 1  | 1  | -1    | -1    | -2 | 0 |
