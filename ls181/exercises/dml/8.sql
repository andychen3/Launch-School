-- SELECT name FROM devices ORDER BY created_at ASC LIMIT 1;


SELECT name FROM devices WHERE created_at = (SELECT min(created_at) FROM devices);
