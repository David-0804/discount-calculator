# 🏷️ Discount Calculator

A lightweight Python utility that applies percentage-based discounts to prices with built-in input validation.

## 📋 Description

This script defines a function that calculates the final price after applying a discount. It includes validation to ensure the inputs are correct before performing the calculation.

## 🚀 How to Run

Make sure you have Python installed, then run:

```bash
python main.py
```

## ⚙️ Function

```python
apply_discount(price, discount)
```

| Parameter | Type | Description |
|---|---|---|
| `price` | `float` or `int` | The original price of the item |
| `discount` | `float` or `int` | The discount percentage to apply (0–100) |

## ✅ Validation Rules

| Condition | Error Message |
|---|---|
| `price` is not a number | `"The price should be a number"` |
| `discount` is not a number | `"The discount should be a number"` |
| `price` is less than or equal to 0 | `"The price should be greater than 0"` |
| `discount` is not between 0 and 100 | `"The discount should be between 0 and 100"` |

## 🧪 Example

```python
print(apply_discount(74.5, 20.0))
```

**Output:**
```
59.6
```

## 📚 Concepts Used

- Functions and parameters
- Type checking with `isinstance()`
- Conditional statements and input validation
- Arithmetic operations

## 📁 File Structure

```
main.py                  # Main script
README.md                # Project documentation
```
