## Statement
The [[Range of a Relation]] $R$, $\textnormal{ran}\\, R$, is a set.

## Explanation

## Proof(s)
Let $R$ be a [[Relation]], and hence by definition a set.\
Let $A = \cup (\cup R)$.\
Since $R$ is a set, applying the [[Axiom of Union]] twice we have that $A$ is a set.\
Notice that by definition of a [[Relation]] and by the [[Axiom of Union]], $\cup R$ is the set of all ordered pairs in $R$, and hence $A = \cup (\cup R)$ is the set of elements of [[Ordered Pair]]s of $R$.\
Recall by definition that an [[Ordered Pair]] $(x, y) = \\{ \\{x\\}, \\{x, y\\}\\}$.\
Then by the [[Axiom Schema of Comprehension]], we can define the set $\\{x \in A \mid \{x\}$ is a singleton $\\}$.\
But this set is exactly those elements in $\textnormal{ran}\, R$, and hence by the [[Axiom of Extensionality]] the two are equal.\
Hence $\textnormal{ran}\\, R$ is a set, as wanted.

## History

## Applications

## Links
### Dependencies
- [[Range of a Relation]]
- [[Axiom of Union]]
- [[Relation]]
- [[Ordered Pair]]
- [[Axiom of Extensionality]]
- [[Axiom Schema of Comprehension]]
### Dependents

## Sources
- Hrbacek, K., & Jech, T. (1999). Introduction to Set Theory, Revised and Expanded (3rd ed.). CRC Press. https://doi.org/10.1201/9781315274096