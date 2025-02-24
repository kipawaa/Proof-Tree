## Statement
If $\kappa_1 = \lvert A_1 \rvert, \lambda_1 = \lvert B_1 \rvert, \kappa_2 = \lvert A_2 \rvert, \lambda_2 = \lvert B_2 \rvert$ such that $A_1 \cap B_1 = \emptyset$ and $A_2 \cap B_2 = \emptyset$ such that $\kappa_1 \leq \kappa_2$ and $\lambda_1 \leq \lambda_2$, then $\kappa_1 + \lambda_1 \leq \kappa_2 + \lambda_2$.

## Explanation

## Proof(s)
Since $\kappa_1 \leq \kappa_2$ we have that there exists an [[Injective Function]] $f : A_1 \to A_2$ by the definiton of [[Ordering of Cardinal Numbers]].\
Since $\lambda_1 \leq \lambda_2$ we have that there exists an [[Injective Function]] $g : B_1 \to B_2$ by the definition of [[Ordering of Cardinal Numbers]].

We define the [[function]] $h : A_1 \cup B_1 \to A_2 \cup B_2$ such that 

$$h(x) = 
\begin{cases} f(x) & x \in A_1\\
 g(x) & x \in B_1 
\end{cases}$$

Since $A_1$ and $B_1$ are [[Disjoint Sets]] we have that $h$ is a [[Function]].\
Since $A_2, B_2$ are [[Disjoint Sets]] we have that $h$ is [[Injective|Injective Function]] since $f$ and $g$ are [[Injective|Injective Function]].\
Hence we have that $\lvert A_1 \cup B_1 \rvert \leq \lvert A_2 \cup B_2 \rvert$ by the definition of [[Ordering of Cardinal Numbers]].\
Hence $\kappa_1 + \lambda_1 \leq \kappa_2 + \lambda_2$, as wanted.

## History

## Applications

## Links
### Dependencies
- [[Function]]
- [[Disjoint Sets]]
- [[Ordering of Cardinal Numbers]]
- [[Injective Function]]
- [[function]]
### Dependents

## Sources
- Hrbacek, K., & Jech, T. (1999). Introduction to Set Theory, Revised and Expanded (3rd ed.). CRC Press. https://doi.org/10.1201/9781315274096
