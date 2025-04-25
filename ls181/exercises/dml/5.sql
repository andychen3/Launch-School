SELECT d.name, COUNT(p.device_id) as number_parts
FROM devices as d
LEFT JOIN parts as p
ON d.id = p.device_id
GROUP BY d.name;