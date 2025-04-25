UPDATE parts SET device_id = 1 WHERE id = 18 OR id = 19;

UPDATE parts SET device_id = 2 WHERE part_number = (SELECT min(part_number) FROM parts);