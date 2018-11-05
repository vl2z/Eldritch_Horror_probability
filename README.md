# Eldritch_Horror_probability
Расчет вероятности победы при броске дайсов в настольной игре "Древний Ужас".

## Пример
Enter human strength (сила): 6

Enter monster toughness (стойкость): 2

Default probability set for [5, 6] as success.
 
 Change probability (y/n)? n
 
Probability to win: 64.88340192043897 %

### Пояснение
Успехами при проверках считаются значения 5 и 6. Для изменения (например, при благословении успехами считается 4, 5, 6) необходимо указать требуемую вероятность (с учетом благословения вероятность будет 3/6).
В примере при силе 6 и стойкости монстра 2, вероятность выкинуть два успеха из шести равна ~65 %.

### Пример с благословением
Enter human strength (сила): 6

Enter monster toughness (стойкость): 2

Default probability set for [5, 6] as success.

 Change probability (y/n)? y
 
Enter new value (ex. 1/6): 3/6

Probability to win: 89.0625 %
