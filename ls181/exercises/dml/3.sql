SELECT d.name, p.part_number
FROM devices d
INNER JOIN parts p
ON d.id = p.device_id;
