SELECT c.name, string_agg(s.description, ', ') as services
FROM customers c
FULL JOIN customers_services cs
ON c.id = cs.customer_id
LEFT JOIN services s
ON s.id = cs.service_id
GROUP BY c.id;

SELECT 
       CASE
        WHEN lag(customers.name) OVER (ORDER BY customers.name, 
        services.description) = customers.name THEN NULL
        ELSE customers.name
       END as name,
       services.description
FROM customers
LEFT OUTER JOIN customers_services
             ON customer_id = customers.id
LEFT OUTER JOIN services
             ON services.id = service_id;