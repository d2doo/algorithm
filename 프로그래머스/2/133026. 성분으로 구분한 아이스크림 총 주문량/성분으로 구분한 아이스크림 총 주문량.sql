SELECT INFO.INGREDIENT_TYPE,SUM(HALF.TOTAL_ORDER) AS TOTAL_ORDER
FROM ICECREAM_INFO INFO
LEFT JOIN FIRST_HALF HALF
ON INFO.FLAVOR = HALF.FLAVOR
GROUP BY INFO.INGREDIENT_TYPE