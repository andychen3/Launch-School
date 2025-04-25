SELECT DISTINCT c.*
FROM customers as c
INNER JOIN customers_services as cs
ON c.id = cs.customer_id;