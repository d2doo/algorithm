SELECT PARENT.ID, 
    IFNULL(
        (
            SELECT COUNT(*)
            FROM ECOLI_DATA CHILD
            WHERE CHILD.PARENT_ID = PARENT.ID
        ), 0) AS CHILD_COUNT
FROM ECOLI_DATA PARENT
ORDER BY ID