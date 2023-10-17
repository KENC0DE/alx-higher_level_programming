-- KEN'S SQL - TMR
-- KEN'S SQL - TMR
SELECT `city`, AVG(`value`) 'avg_temp' FROM temperatures GROUP BY `city` ORDER BY `avg_temp` DESC;
