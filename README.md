# IS218 Design Patterns Stats Calculator
Extending the original OOP calculator.

## Part 2 Question

**Where does the construction policy of the newly added operation live?**

It lives in CalculationFactory.operations in calculator/factory.py.

**Explain creation versus execution without using the words factory or pattern**

Creation refers to creating the calculation object that holds references to the operands and the operation, whereas executing a calculation refers to actually using the information stored in the references of the calculation object to complete the operation.

## Part 1 Questions

**One corrected prediction**

Before doing this section, I did not know that these ites needed to be seperated- I thought contructing a Calculation would immediatley perform the math, however now I know that storing the oeprands and operation is seperate, and get_result() exectes the operation later.

**What does self refer to?**

Self refers to the calculation object who is handling the numbers before passing them to Operations.

**Why is operations static?**

It is static so that it does not need to instantiated to use its methods.

**What happens immediatley after construction?**

After the construction of the calculation object, its numbers are validated and stored, and its operation is stored.

**Why store result with the calculation?**

So that History can display the recorded result without re-reunning the calculation.

## Notes from throughout the stages

**Add and subtract need seperate get_result() implementations even though the only difference is the selected math function bc...**

The two classes are almost exactly the same, so instead of making a specific add or subtract object, we can make it a general calculation, and choose which general calculation operation we want to use.
"Instead of making a different class for every operation, make ONE Calculation class that can be given different operations."

