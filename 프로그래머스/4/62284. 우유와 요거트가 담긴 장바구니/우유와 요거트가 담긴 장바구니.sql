-- 코드를 입력하세요
SELECT 
    CART_ID
FROM CART_PRODUCTS
WHERE NAME LIKE '%Milk%' OR NAME LIKE '%Yogurt%'
GROUP BY CART_ID
HAVING COUNT(DISTINCT NAME) >= 2
ORDER BY ID	