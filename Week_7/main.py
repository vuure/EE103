import even_or_odd
import calc
import countEvenNumbers

m_num = 5

even_or_odd_alias = even_or_odd.evenOrOdd

even_or_odd_result = even_or_odd_alias(m_num)

print(even_or_odd_result)

calc_result = calc.calculator("add", 10, 5)
print(calc_result)

even_count = countEvenNumbers.countEven(even_or_odd.evenOrOdd, m_num)
print(even_count)

evenOrNot_lambda = lambda x : "Even" if x % 2 == 0 else "Odd"

