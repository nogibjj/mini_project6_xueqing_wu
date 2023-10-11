```sql
UPDATE Birth SET 
        Year=1, 
        Month=1,
        Day_Of_Month=1,
        Day_Of_Week=1, 
        Births=1, 
        WHERE id=2;
```

```sql
DELETE FROM Birth WHERE id=1;
```

```sql
SELECT * FROM Birth;
```

```sql
UPDATE Birth SET 
        Year=2000, 
        Month=1,
        Day_Of_Month=1,
        Day_Of_Week=6, 
        Births=9083, 
        WHERE id=1;
```

```sql
DELETE FROM Birth WHERE id=1;
```

```sql
INSERT INTO ServeTimesDB VALUES (
            2000, 
            1, 
            1, 
            6, 
            9083
            );
```

```sql
SELECT * FROM Birth WHERE Year = '2000'
```

```sql
SELECT * FROM Birth;
```

```sql
SELECT * FROM Birth WHERE Year='2000';
```

```sql
UPDATE Birth SET 
        Year=2000, 
        Month=1,
        Day_Of_Month=1,
        Day_Of_Week=6, 
        Births=9083, 
        WHERE id=1;
```

```sql
DELETE FROM Birth WHERE id=1;
```

```sql
INSERT INTO ServeTimesDB VALUES (
            2000, 
            1, 
            1, 
            6, 
            9083
            );
```

```sql
SELECT * FROM Birth WHERE Year = '2000'
```

```sql
SELECT * FROM Birth;
```

```sql
INSERT INTO ServeTimesDB VALUES (
            2000, 
            1, 
            1, 
            6, 
            9083
            );
```

```sql
SELECT * FROM Birth;
```

```sql
UPDATE Birth SET 
        Year=2000, 
        Month=1,
        Day_Of_Month=1,
        Day_Of_Week=6, 
        Births=9083, 
        WHERE id=1;
```

```sql
DELETE FROM Birth WHERE id=1;
```

```sql
SELECT * FROM Birth WHERE Year = '2000'
```

```sql
SELECT * FROM Birth WHERE Year='2000';
```

```sql
UPDATE Birth SET 
        Year=2000, 
        Month=1,
        Day_Of_Month=1,
        Day_Of_Week=6, 
        Births=9083, 
        WHERE id=1;
```

```sql
DELETE FROM Birth WHERE id=1;
```

```sql
INSERT INTO ServeTimesDB VALUES (
            2000, 
            1, 
            1, 
            6, 
            9083
            );
```

```sql
SELECT * FROM Birth WHERE Year = '2000'
```

```sql
SELECT * FROM Birth;
```

```sql
INSERT INTO ServeTimesDB VALUES (
            2000, 
            1, 
            1, 
            6, 
            9083
            );
```

```sql
SELECT * FROM Birth;
```

```sql
UPDATE Birth SET 
        Year=2000, 
        Month=1,
        Day_Of_Month=1,
        Day_Of_Week=6, 
        Births=9083, 
        WHERE id=1;
```

```sql
DELETE FROM Birth WHERE id=1;
```

```sql
SELECT * FROM Birth WHERE Year = '2000'
```

```sql
Select Year, Month, Day_Of_Month, sum(births) as The_Number_of_Birth FROM birth1 INNER JOIN birth2 ON birth1.id = birth2.id Group By Year, Month, Day_Of_Month ORDER BY The_Number_of_Birth Desc LIMIT 10
```

```response from databricks
[Row(Year=2000, Month=1, Day_Of_Month=4, The_Number_of_Birth=13032), Row(Year=2000, Month=1, Day_Of_Month=11, The_Number_of_Birth=12611), Row(Year=2000, Month=1, Day_Of_Month=25, The_Number_of_Birth=12593), Row(Year=2000, Month=1, Day_Of_Month=5, The_Number_of_Birth=12558), Row(Year=2000, Month=1, Day_Of_Month=7, The_Number_of_Birth=12516), Row(Year=2000, Month=1, Day_Of_Month=20, The_Number_of_Birth=12506), Row(Year=2000, Month=1, Day_Of_Month=6, The_Number_of_Birth=12466), Row(Year=2000, Month=1, Day_Of_Month=27, The_Number_of_Birth=12408), Row(Year=2000, Month=1, Day_Of_Month=19, The_Number_of_Birth=12405), Row(Year=2000, Month=1, Day_Of_Month=12, The_Number_of_Birth=12398)]
```

```sql
<<<<<<< HEAD
=======
Select Year, Month, Day_Of_Month, sum(births) as The_Number_of_Birth FROM birth1 INNER JOIN birth2 ON birth1.id = birth2.id Group By Year, Month, Day_Of_Month ORDER BY The_Number_of_Birth Desc LIMIT 10
```

```response from databricks
[Row(Year=2000, Month=1, Day_Of_Month=4, The_Number_of_Birth=13032), Row(Year=2000, Month=1, Day_Of_Month=11, The_Number_of_Birth=12611), Row(Year=2000, Month=1, Day_Of_Month=25, The_Number_of_Birth=12593), Row(Year=2000, Month=1, Day_Of_Month=5, The_Number_of_Birth=12558), Row(Year=2000, Month=1, Day_Of_Month=7, The_Number_of_Birth=12516), Row(Year=2000, Month=1, Day_Of_Month=20, The_Number_of_Birth=12506), Row(Year=2000, Month=1, Day_Of_Month=6, The_Number_of_Birth=12466), Row(Year=2000, Month=1, Day_Of_Month=27, The_Number_of_Birth=12408), Row(Year=2000, Month=1, Day_Of_Month=19, The_Number_of_Birth=12405), Row(Year=2000, Month=1, Day_Of_Month=12, The_Number_of_Birth=12398)]
```

```sql
Select  Year, Month, 	Day_Of_Month,  sum(births) as The_Number_of_Birth
            FROM birth1 INNER JOIN birth2 ON birth1.id = birth2.id
            Group By Year, Month, Day_Of_Month
            ORDER BY The_Number_of_Birth Desc
            LIMIT 10
```

```response from databricks
[Row(Year=2000, Month=1, Day_Of_Month=4, The_Number_of_Birth=13032), Row(Year=2000, Month=1, Day_Of_Month=11, The_Number_of_Birth=12611), Row(Year=2000, Month=1, Day_Of_Month=25, The_Number_of_Birth=12593), Row(Year=2000, Month=1, Day_Of_Month=5, The_Number_of_Birth=12558), Row(Year=2000, Month=1, Day_Of_Month=7, The_Number_of_Birth=12516), Row(Year=2000, Month=1, Day_Of_Month=20, The_Number_of_Birth=12506), Row(Year=2000, Month=1, Day_Of_Month=6, The_Number_of_Birth=12466), Row(Year=2000, Month=1, Day_Of_Month=27, The_Number_of_Birth=12408), Row(Year=2000, Month=1, Day_Of_Month=19, The_Number_of_Birth=12405), Row(Year=2000, Month=1, Day_Of_Month=12, The_Number_of_Birth=12398)]
```

```sql
>>>>>>> 9f4ee0e4be233587bdc5ed1319f68d47b70eb017
Select  Year, Month, 	Day_Of_Month,  sum(births) as The_Number_of_Birth
            FROM birth1 INNER JOIN birth2 ON birth1.id = birth2.id
            Group By Year, Month, Day_Of_Month
            ORDER BY The_Number_of_Birth Desc
            LIMIT 10
```

```response from databricks
[Row(Year=2000, Month=1, Day_Of_Month=4, The_Number_of_Birth=13032), Row(Year=2000, Month=1, Day_Of_Month=11, The_Number_of_Birth=12611), Row(Year=2000, Month=1, Day_Of_Month=25, The_Number_of_Birth=12593), Row(Year=2000, Month=1, Day_Of_Month=5, The_Number_of_Birth=12558), Row(Year=2000, Month=1, Day_Of_Month=7, The_Number_of_Birth=12516), Row(Year=2000, Month=1, Day_Of_Month=20, The_Number_of_Birth=12506), Row(Year=2000, Month=1, Day_Of_Month=6, The_Number_of_Birth=12466), Row(Year=2000, Month=1, Day_Of_Month=27, The_Number_of_Birth=12408), Row(Year=2000, Month=1, Day_Of_Month=19, The_Number_of_Birth=12405), Row(Year=2000, Month=1, Day_Of_Month=12, The_Number_of_Birth=12398)]
```

```sql
Select Year, Month, Day_Of_Month, sum(births) as The_Number_of_Birth FROM birth1 INNER JOIN birth2 ON birth1.id = birth2.id Group By Year, Month, Day_Of_Month ORDER BY The_Number_of_Birth Desc LIMIT 10
```

```response from databricks
[Row(Year=2000, Month=1, Day_Of_Month=4, The_Number_of_Birth=13032), Row(Year=2000, Month=1, Day_Of_Month=11, The_Number_of_Birth=12611), Row(Year=2000, Month=1, Day_Of_Month=25, The_Number_of_Birth=12593), Row(Year=2000, Month=1, Day_Of_Month=5, The_Number_of_Birth=12558), Row(Year=2000, Month=1, Day_Of_Month=7, The_Number_of_Birth=12516), Row(Year=2000, Month=1, Day_Of_Month=20, The_Number_of_Birth=12506), Row(Year=2000, Month=1, Day_Of_Month=6, The_Number_of_Birth=12466), Row(Year=2000, Month=1, Day_Of_Month=27, The_Number_of_Birth=12408), Row(Year=2000, Month=1, Day_Of_Month=19, The_Number_of_Birth=12405), Row(Year=2000, Month=1, Day_Of_Month=12, The_Number_of_Birth=12398)]
```

```sql
Select  Year, Month, 	Day_Of_Month,  sum(births) as The_Number_of_Birth
            FROM birth1 INNER JOIN birth2 ON birth1.id = birth2.id
            Group By Year, Month, Day_Of_Month
            ORDER BY The_Number_of_Birth Desc
            LIMIT 10
```

```response from databricks
[Row(Year=2000, Month=1, Day_Of_Month=4, The_Number_of_Birth=13032), Row(Year=2000, Month=1, Day_Of_Month=11, The_Number_of_Birth=12611), Row(Year=2000, Month=1, Day_Of_Month=25, The_Number_of_Birth=12593), Row(Year=2000, Month=1, Day_Of_Month=5, The_Number_of_Birth=12558), Row(Year=2000, Month=1, Day_Of_Month=7, The_Number_of_Birth=12516), Row(Year=2000, Month=1, Day_Of_Month=20, The_Number_of_Birth=12506), Row(Year=2000, Month=1, Day_Of_Month=6, The_Number_of_Birth=12466), Row(Year=2000, Month=1, Day_Of_Month=27, The_Number_of_Birth=12408), Row(Year=2000, Month=1, Day_Of_Month=19, The_Number_of_Birth=12405), Row(Year=2000, Month=1, Day_Of_Month=12, The_Number_of_Birth=12398)]
```

```sql
Select  Year, Month, 	Day_Of_Month,  sum(births) as The_Number_of_Birth
            FROM birth1 INNER JOIN birth2 ON birth1.id = birth2.id
            Group By Year, Month, Day_Of_Month
            ORDER BY The_Number_of_Birth Desc
            LIMIT 10
```

```response from databricks
[Row(Year=2000, Month=1, Day_Of_Month=4, The_Number_of_Birth=13032), Row(Year=2000, Month=1, Day_Of_Month=11, The_Number_of_Birth=12611), Row(Year=2000, Month=1, Day_Of_Month=25, The_Number_of_Birth=12593), Row(Year=2000, Month=1, Day_Of_Month=5, The_Number_of_Birth=12558), Row(Year=2000, Month=1, Day_Of_Month=7, The_Number_of_Birth=12516), Row(Year=2000, Month=1, Day_Of_Month=20, The_Number_of_Birth=12506), Row(Year=2000, Month=1, Day_Of_Month=6, The_Number_of_Birth=12466), Row(Year=2000, Month=1, Day_Of_Month=27, The_Number_of_Birth=12408), Row(Year=2000, Month=1, Day_Of_Month=19, The_Number_of_Birth=12405), Row(Year=2000, Month=1, Day_Of_Month=12, The_Number_of_Birth=12398)]
```

```sql
Select Year, Month, Day_Of_Month, sum(births) as The_Number_of_Birth FROM birth1 INNER JOIN birth2 ON birth1.id = birth2.id Group By Year, Month, Day_Of_Month ORDER BY The_Number_of_Birth Desc LIMIT 10
```

```response from databricks
[Row(Year=2000, Month=1, Day_Of_Month=4, The_Number_of_Birth=13032), Row(Year=2000, Month=1, Day_Of_Month=11, The_Number_of_Birth=12611), Row(Year=2000, Month=1, Day_Of_Month=25, The_Number_of_Birth=12593), Row(Year=2000, Month=1, Day_Of_Month=5, The_Number_of_Birth=12558), Row(Year=2000, Month=1, Day_Of_Month=7, The_Number_of_Birth=12516), Row(Year=2000, Month=1, Day_Of_Month=20, The_Number_of_Birth=12506), Row(Year=2000, Month=1, Day_Of_Month=6, The_Number_of_Birth=12466), Row(Year=2000, Month=1, Day_Of_Month=27, The_Number_of_Birth=12408), Row(Year=2000, Month=1, Day_Of_Month=19, The_Number_of_Birth=12405), Row(Year=2000, Month=1, Day_Of_Month=12, The_Number_of_Birth=12398)]
```

```sql
Select  Year, Month, 	Day_Of_Month,  sum(births) as The_Number_of_Birth
            FROM birth1 INNER JOIN birth2 ON birth1.id = birth2.id
            Group By Year, Month, Day_Of_Month
            ORDER BY The_Number_of_Birth Desc
            LIMIT 10
```

```response from databricks
[Row(Year=2000, Month=1, Day_Of_Month=4, The_Number_of_Birth=13032), Row(Year=2000, Month=1, Day_Of_Month=11, The_Number_of_Birth=12611), Row(Year=2000, Month=1, Day_Of_Month=25, The_Number_of_Birth=12593), Row(Year=2000, Month=1, Day_Of_Month=5, The_Number_of_Birth=12558), Row(Year=2000, Month=1, Day_Of_Month=7, The_Number_of_Birth=12516), Row(Year=2000, Month=1, Day_Of_Month=20, The_Number_of_Birth=12506), Row(Year=2000, Month=1, Day_Of_Month=6, The_Number_of_Birth=12466), Row(Year=2000, Month=1, Day_Of_Month=27, The_Number_of_Birth=12408), Row(Year=2000, Month=1, Day_Of_Month=19, The_Number_of_Birth=12405), Row(Year=2000, Month=1, Day_Of_Month=12, The_Number_of_Birth=12398)]
```

```sql
Select  Year, Month, 	Day_Of_Month,  sum(births) as The_Number_of_Birth
            FROM birth1 INNER JOIN birth2 ON birth1.id = birth2.id
            Group By Year, Month, Day_Of_Month
            ORDER BY The_Number_of_Birth Desc
            LIMIT 10
```

```response from databricks
[Row(Year=2000, Month=1, Day_Of_Month=4, The_Number_of_Birth=13032), Row(Year=2000, Month=1, Day_Of_Month=11, The_Number_of_Birth=12611), Row(Year=2000, Month=1, Day_Of_Month=25, The_Number_of_Birth=12593), Row(Year=2000, Month=1, Day_Of_Month=5, The_Number_of_Birth=12558), Row(Year=2000, Month=1, Day_Of_Month=7, The_Number_of_Birth=12516), Row(Year=2000, Month=1, Day_Of_Month=20, The_Number_of_Birth=12506), Row(Year=2000, Month=1, Day_Of_Month=6, The_Number_of_Birth=12466), Row(Year=2000, Month=1, Day_Of_Month=27, The_Number_of_Birth=12408), Row(Year=2000, Month=1, Day_Of_Month=19, The_Number_of_Birth=12405), Row(Year=2000, Month=1, Day_Of_Month=12, The_Number_of_Birth=12398)]
```

```sql
Select Year, Month, Day_Of_Month, sum(births) as The_Number_of_Birth FROM birth1 INNER JOIN birth2 ON birth1.id = birth2.id Group By Year, Month, Day_Of_Month ORDER BY The_Number_of_Birth Desc LIMIT 10
```

```response from databricks
[Row(Year=2000, Month=1, Day_Of_Month=4, The_Number_of_Birth=13032), Row(Year=2000, Month=1, Day_Of_Month=11, The_Number_of_Birth=12611), Row(Year=2000, Month=1, Day_Of_Month=25, The_Number_of_Birth=12593), Row(Year=2000, Month=1, Day_Of_Month=5, The_Number_of_Birth=12558), Row(Year=2000, Month=1, Day_Of_Month=7, The_Number_of_Birth=12516), Row(Year=2000, Month=1, Day_Of_Month=20, The_Number_of_Birth=12506), Row(Year=2000, Month=1, Day_Of_Month=6, The_Number_of_Birth=12466), Row(Year=2000, Month=1, Day_Of_Month=27, The_Number_of_Birth=12408), Row(Year=2000, Month=1, Day_Of_Month=19, The_Number_of_Birth=12405), Row(Year=2000, Month=1, Day_Of_Month=12, The_Number_of_Birth=12398)]
```

```sql
Select  Year, Month, 	Day_Of_Month,  sum(births) as The_Number_of_Birth
            FROM birth1 INNER JOIN birth2 ON birth1.id = birth2.id
            Group By Year, Month, Day_Of_Month
            ORDER BY The_Number_of_Birth Desc
            LIMIT 10
```

```response from databricks
[Row(Year=2000, Month=1, Day_Of_Month=4, The_Number_of_Birth=13032), Row(Year=2000, Month=1, Day_Of_Month=11, The_Number_of_Birth=12611), Row(Year=2000, Month=1, Day_Of_Month=25, The_Number_of_Birth=12593), Row(Year=2000, Month=1, Day_Of_Month=5, The_Number_of_Birth=12558), Row(Year=2000, Month=1, Day_Of_Month=7, The_Number_of_Birth=12516), Row(Year=2000, Month=1, Day_Of_Month=20, The_Number_of_Birth=12506), Row(Year=2000, Month=1, Day_Of_Month=6, The_Number_of_Birth=12466), Row(Year=2000, Month=1, Day_Of_Month=27, The_Number_of_Birth=12408), Row(Year=2000, Month=1, Day_Of_Month=19, The_Number_of_Birth=12405), Row(Year=2000, Month=1, Day_Of_Month=12, The_Number_of_Birth=12398)]
```

```sql
Select  Year, Month, 	Day_Of_Month,  sum(births) as The_Number_of_Birth
            FROM birth1 INNER JOIN birth2 ON birth1.id = birth2.id
            Group By Year, Month, Day_Of_Month
            ORDER BY The_Number_of_Birth Desc
            LIMIT 10
```

```response from databricks
[Row(Year=2000, Month=1, Day_Of_Month=4, The_Number_of_Birth=13032), Row(Year=2000, Month=1, Day_Of_Month=11, The_Number_of_Birth=12611), Row(Year=2000, Month=1, Day_Of_Month=25, The_Number_of_Birth=12593), Row(Year=2000, Month=1, Day_Of_Month=5, The_Number_of_Birth=12558), Row(Year=2000, Month=1, Day_Of_Month=7, The_Number_of_Birth=12516), Row(Year=2000, Month=1, Day_Of_Month=20, The_Number_of_Birth=12506), Row(Year=2000, Month=1, Day_Of_Month=6, The_Number_of_Birth=12466), Row(Year=2000, Month=1, Day_Of_Month=27, The_Number_of_Birth=12408), Row(Year=2000, Month=1, Day_Of_Month=19, The_Number_of_Birth=12405), Row(Year=2000, Month=1, Day_Of_Month=12, The_Number_of_Birth=12398)]
```

