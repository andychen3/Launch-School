SELECT sum(s.price) as gross
FROM services s
INNER JOIN customers_services cs
ON s.id = cs.service_id;