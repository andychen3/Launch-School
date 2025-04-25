SELECT c.*
FROM customers c
LEFT JOIN customers_services cs
ON c.id = cs.customer_id
WHERE cs.service_id IS NULL;


# Further exploration
SELECT c.*, s.*
FROM customers c
FULL JOIN customers_services cs
ON c.id = cs.customer_id
FULL JOIN services s
ON cs.service_id = s.id
WHERE cs.service_id IS NULL or cs.customer_id IS NULL;