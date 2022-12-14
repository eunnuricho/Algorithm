SELECT T1.CATEGORY, T1.MAX_PRICE, T2.PRODUCT_NAME

FROM (SELECT CATEGORY, MAX(PRICE) AS MAX_PRICE
      FROM FOOD_PRODUCT
      WHERE CATEGORY IN ('과자', '국', '김치', '식용유')
      GROUP BY CATEGORY) AS T1

INNER JOIN (SELECT * FROM FOOD_PRODUCT) AS T2
ON T1.CATEGORY = T2.CATEGORY AND T1.MAX_PRICE = T2.PRICE
ORDER BY T1.MAX_PRICE DESC;