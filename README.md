# Unique Elements Checker

Цей проєкт містить функцію на Python для перевірки, чи всі елементи в списку є унікальними.

## Опис

Функція `is_unique(lst)` приймає список `lst` і повертає:
- `True` — якщо всі елементи унікальні;
- `False` — якщо є повторення.

## Приклад використання

```python
from is_unique import is_unique

print(is_unique([1, 2, 3]))       # True
print(is_unique([1, 2, 2]))       # False
