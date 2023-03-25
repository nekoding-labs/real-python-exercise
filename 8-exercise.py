# 1. Print the result of the calculation 3 ** .125 as a fixed-point number
# with three decimal places.

# 2. Print the number 150000 as currency, with the thousands grouped
# with commas. Currency should be displayed with two decimal
# places.

# 3. Print the result of 2 / 10 as a percentage with no decimal places.
# The output should look like 20%.

n = 3 ** .125
print(f"{n:.3f}")

a = 150_000
print(f"{a:,.2f}")

b = 2 / 10 * 100
print(f"{b:.0f}%")
