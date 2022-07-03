# 100 prisoners problem in Python
 Solution (best strategy) in Python to solve the 100 prisoners problem. The script also includes the random picks strategy.

[Wikipedia - 100 prisoners problem](https://en.wikipedia.org/wiki/100_prisoners_problem)

- - -

#### `no_strategy()`
Every prisoner selects randomly 50 boxes, which leads to a success rate of  $ (\frac{1}{2})^{100} \approx 0.0000000000000000000000000000008 $%.

#### `solution()`
Each prisoner starts by opening the box with his own number. If it contains his number he is done, otherwise, he will open the box with the number that he found before and so on. Surprisingly, the probability of success is more than  $ 30 $%.
