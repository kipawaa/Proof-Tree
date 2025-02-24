## Statement
If $(W, <)$ is a [[Well-Ordered Set]] and $S$ is an [[Initial Segment]] of $W$, then there exists an element $a \in W$ such that $S = \{x \in W \mid x < a\}$.

## Explanation

## Proof(s)
Let $X = W \setminus S$, i.e. $X = \{x \in W \mid x \notin S\}$.\
Since an [[Initial Segment]] must be proper subset, we have that $X \neq \emptyset$.\
Since $W$ is [[Well-Ordered|Well-Ordered Set]] we have that $X$ has a [[Least Element]] $a$.\
Hence we can define the set $\{x \in W \mid x < a\}$.

Let $y \in S$.\
Suppose that $y \not < a$.\
Then $y = a$ or $a < y$.

If $y = a$ then we have that $a = y \in S$, hence $a \in S$.\
But $a \in X = W \setminus S$, hence $a \notin S$, a contradiction.

If $a < y$ then by definition of [[Initial Segment]] we have that $a \in S$.\
But again we have that $a \in X = W \setminus S$ hence $a \notin S$, a contradiction.

Hence $y < a$ and we have that $S \subseteq \{x \in W \mid x < a\}$.

Let $y \in \{x \in W \mid x < a\}$.\
Then by definition of this set we have that $y \in W$ and $y < a$.\
Since $a$ is the least element of $X$ and $y < a$, we have that $y \notin X$.\
Hence $y \in W \setminus X = W \setminus (W \setminus S) = S$.\
Hence $\{x \in W \mid x < a\} \subseteq S$.

Hence $S = \{x \in W \mid x < a\}$, as wanted.

## History

## Applications

## Links
### Dependencies
- [[Initial Segment]]
- [[Least Element]]
### Dependents

## Sources
- Hrbacek, K., & Jech, T. (1999). Introduction to Set Theory, Revised and Expanded (3rd ed.). CRC Press. https://doi.org/10.1201/9781315274096
