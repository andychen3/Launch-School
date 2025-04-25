SELECT s.description
FROM customers_services cs
RIGHT JOIN services s
ON s.id = cs.service_id
WHERE cs.service_id IS NULL;