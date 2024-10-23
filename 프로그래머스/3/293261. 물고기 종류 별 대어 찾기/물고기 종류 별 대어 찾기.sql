SELECT INFO.ID, NAME.FISH_NAME, INFO.LENGTH
FROM FISH_INFO INFO
JOIN FISH_NAME_INFO NAME ON INFO.FISH_TYPE = NAME.FISH_TYPE
WHERE INFO.LENGTH = (
    SELECT MAX(INFO2.LENGTH)
    FROM FISH_INFO INFO2
    WHERE INFO2.FISH_TYPE = INFO.FISH_TYPE
)