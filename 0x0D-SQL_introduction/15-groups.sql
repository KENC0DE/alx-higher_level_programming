-- KEN'S SQL - TMR
SELECT `score`, COUNT(`score`) 'number' FROM `second_table` GROUP BY `score` ORDER BY `number` DESC;
