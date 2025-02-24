## Statement
The [[Integers]] are [[Countable]].

## Explanation

## Proof(s)
Consider the function $f : \mathbb{N} \to \mathbb{Z}$ given by 
    
$$f(n) = 
\begin{cases} \frac{n}{2} & n \text{ even}\\
 -\frac{n+1}{2} & n \text{ odd}
\end{cases}.$$

### $f$ is Injective
Suppose that $f(n) = f(m)$.\\

If $n$ is even then $f(n) = f(m) \implies \frac{n}{2} = f(m)$.\\
If $m$ is odd then we have that $f(m) < 0 \implies \frac{n}{2} < 0$, a contradiction.\\
Hence $m$ is even and we have that $f(m) = \frac{m}{2}$.\\
This gives that $\frac{n}{2} = \frac{m}{2} \implies m = n$.

If $n$ is odd then $f(n) = f(m) \implies -\frac{n+1}{2} = f(m)$.\\
If $m$ is even then $f(m) \geq 0 \implies f(n) \geq 0$, a contradiction.\\
Hence $m$ is odd and we have that $f(m) = -\frac{m+1}{2}$.\\
This gives that $-\frac{n+1}{2} = -\frac{m+1}{2} \implies n = m$.

Hence $f$ is injective.

### $f$ is Surjective
Suppose that $\nexists n \in \mathbb{N}$ such that $f(n) = z$ for some $z \in \mathbb{Z}$.\\
Notice that since $z \in \mathbb{Z}$, $z \geq 0$ or $z < 0$.\\

If $z < 0$ then $z = -k$ for some $k \in \mathbb{N}$.\\
Notice that $\forall k \in \mathbb{N}, \exists n$ such that $k = \frac{n+1}{2}$.\\
Hence $z = -k = -\frac{n+1}{2}$.

If $z \geq 0$ then $z \in \mathbb{N}$.\\
For all $k \in \mathbb{N}, \exists n$ such that $k = \frac{n}{2}$.\\
Hence $\exists n$ such that $z = \frac{n}{2}$.

Therefore $f$ is surjective

Since $f$ is injective and surjective, we have that $f : \mathbb{N} \to \mathbb{Z}$ is a bijection.\\
Hence $\mathbb{Z}$ is countable, as wanted.

## History

## Applications

## Links
### Dependencies
- [[Countable]]
- [[Integers]]
### Dependents

## Sources
- Hrbacek, K., & Jech, T. (1999). Introduction to Set Theory, Revised and Expanded (3rd ed.). CRC Press. https://doi.org/10.1201/9781315274096
