SELECT SUM(s.price)
FROM services s
INNER JOIN customers_services cs
ON s.id = cs.service_id
WHERE s.price >= 100;

SELECT SUM(price)
FROM customers
CROSS JOIN services
WHERE price > 100;