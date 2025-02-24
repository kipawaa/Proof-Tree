## Statement
If $\alpha$ is an [[Ordinal|Ordinal Numbers]], then $S(\alpha)$, the [[Successor]] of $\alpha$, is an [[Ordinal|Ordinal Numbers]].

## Explanation

## Proof(s)
Suppose that $\alpha$ is an [[Ordinal|Ordinal Numbers]].\
Consider the [[Successor]] of $\alpha$, $S(\alpha)$.

We first show that $S(\alpha)$ is [[Transitive|Transitive Set]].\
Let $\beta \in S(\alpha)$ (notice that by definition of [[Successor]], $S(\alpha)$ is [[non-empty|Empty Set]].\
Then by definition of $S(\alpha)$, $\beta \in \alpha$ or $\beta = \alpha$.

If $\beta = \alpha$ then by definition of [[Successor]] we have that $\beta = \alpha \subset \alpha \cup \\{\alpha\\} = S(\alpha)$.

If $\beta \in \alpha$ then since $\alpha$ is [[Transitive|Transitive Set]] we have that $\beta \subset \alpha$.\
Hence since $\alpha \subset S(\alpha)$ we have that $\beta \subset S(\alpha)$.\
Hence $S(\alpha)$ is [[Transitive|Transitive Set]].

We now show that $S(\alpha)$ is well-ordered by membership.

First, $\in \mid_{S(\alpha)}$ is [[Transitive|Transitive Relation]].\
Let $x, y, z \in S(\alpha)$ such that $x \in y$ and $y \in z$.\
By definition of [[Successor]], since $z \in S(\alpha)$ we have that $z \in \alpha$ or $z = \alpha$.\
By the [[Axiom of Regularity]] we have that both of these cannot happen.\
If $z = \alpha$ then $y \in \alpha$.\
By [[Transitivity|Transitive Set]] of $\alpha$ we have that $y \subset \alpha$.\
Since $x \in y \subset \alpha$ we have that $x \in \alpha$.\
Since $z = \alpha$ we have that $x \in z$.

If $z \in \alpha$ then since $\alpha$ is and [[Ordinal|Ordinal Numbers]] and hence [[Transitive|Transitive Set]], we have that $z \subset \alpha$.\
Since $y \in z$ and $z \subset \alpha$ we have that $y \in \alpha$.\
Since $\alpha$ is [[Transitive|Transitive Set]] we have that $y \subset \alpha$.\
Since $x \in y$ and $y \subset \alpha$ we have that $x \in \alpha$.\
Hence we have that $x, y, z \in \alpha$.\
Since $\alpha$ is an [[Ordinal|Ordinal Numbers]] we have that $\in\mid_\alpha$ is [[Transitive|Transitive Relation]] and hence $x \in z$.\
Therefore $\in\mid_{S(\alpha)}$ is [[Transitive|Transitive Relation]].

Second, $\in \mid_{S(\alpha)}$ is [[Asymmetric|Asymmetric Relation]].\
Let $x, y \in S(\alpha)$, and hence by definition of [[Successor]], $x \in \alpha$ or $x = \alpha$ and similarly for $y$.

If $x, y \in \alpha$ then since $\alpha$ is an [[Ordinal|Ordinal Numbers]] we have that $\in \mid_{S(\alpha)} = \in\mid_{\alpha}$ which is [[Asymmetric|Asymmetric Relation]].

If $x \in \alpha$ and $y = \alpha$ then clearly $x \in \alpha = y \implies x \in y$.\
Suppose $y \in x$.\
Then $\alpha = y \in x$.\
Since $x \in \alpha$ and $\alpha$ is an [[Ordinal|Ordinal Numbers]] and hence [[Transitive|Transitive Set]], we have that $x \subset \alpha$.\
Then $\alpha = y \in x \subset \alpha$ gives that $\alpha \in \alpha$, which contradicts that [[No Set Contains Itself]].\
Hence $y \notin x$.\
The case for $x = \alpha$ and $y \in \alpha$ is analogous.

If $x = y = \alpha$ then if $x \in y$ or $y \in x$ then $\alpha \in \alpha$, which contradicts that [[No Set Contains Itself]].\
Hence $x \notin y$ and $y \notin x$.
Therefore $\in\mid_{S(\alpha)}$ is [[Asymmetric|Asymmetric Relation]].

Lastly, we show that elements of $S(\alpha)$ are [[Comparable]].\
Let $x, y \in S(\alpha)$.

Notice that if $x = y$ then they are clearly [[Comparable]].

If $x \neq y$ and $x, y \in \alpha$ then $x$ and $y$ are comparable since elements of $\alpha$ are comparable because $\alpha$ is an [[Ordinal|Ordinal Numbers]] and hence [[Well-Ordered|Well-Ordered Set]] and hence [[Linearly Ordered|Linear Ordering]].\
If $x \neq y$ and $x = \alpha$ then $y \in x$ and hence $x, y$ are [[Comparable]].\
Hence elements of $S(\alpha)$ are comparable.

Lastly, we show that $S(\alpha)$ is a [[Well Ordered Set]] by $\in\mid_{S(\alpha)}$.\
Let $A$ be a [[non-empty|Empty Set]] subset of $S(\alpha)$.\
If $A \subseteq \alpha$ then since $\alpha$ is a [[Well Ordered Set]] there is a [[Least Element]] of $A$ with respect to $\in\mid_\alpha$, which is equivalent to $\in\mid_{S(\alpha)}$ on $A$.

If $A = \\{\alpha\\}$ then $\alpha$ is the only element of $A$ and hence the [[Least Element]] of $A$ with respect to $\in\mid_{S(\alpha)}$.

If $A \subseteq S(\alpha)$ then $A \setminus \\{\alpha\\}$ is a subset of $\alpha$ and hence has a [[Least Element]] since $\alpha$ is a [[Well-Ordered Set]] with respect to $\in\mid_\alpha$.\
Notice that this [[Least Element]] is an element of $\alpha$ and hence is a [[Least Element]] of $A$ with respect to $\in\mid_{S(\alpha)}$.\
Hence $S(\alpha)$ is a [[Well-Ordered Set]] with respect to $\in\mid_{S(\alpha)}$.

Hence $S(\alpha)$ is an [[Ordinal|Ordinal Numbers]], as wanted.

## History

## Applications

## Links
### Dependencies
- [[No Set Contains Itself]]
- [[Successor]]
- [[Well Ordered Set]]
- [[Axiom of Regularity]]
- [[Transitive Relation]]
- [[Asymmetric Relation]]
- [[Comparable]]
- [[Ordinal Numbers]]
- [[Least Element]]
- [[Transitive Set]]
- [[Linear Ordering]]
### Dependents

## Sources
- Hrbacek, K., & Jech, T. (1999). Introduction to Set Theory, Revised and Expanded (3rd ed.). CRC Press. https://doi.org/10.1201/9781315274096
