WITH MAX_SIZE_OF_COLONY AS (
    SELECT MAX(SIZE_OF_COLONY) AS MAX_SIZE, YEAR(DIFFERENTIATION_DATE) AS YEAR
    FROM ECOLI_DATA
    GROUP BY YEAR
)

SELECT YEAR(ED.DIFFERENTIATION_DATE) AS YEAR
    , (MS.MAX_SIZE - ED.SIZE_OF_COLONY) AS YEAR_DEV
    , ID
FROM MAX_SIZE_OF_COLONY MS
JOIN ECOLI_DATA ED ON YEAR(ED.DIFFERENTIATION_DATE) = MS.YEAR
ORDER BY `YEAR` ASC, `YEAR_DEV` ASC;