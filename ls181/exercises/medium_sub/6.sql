SELECT name, (SELECT count(item_id) from bids WHERE item_id = items.id) FROM items;

SELECT items.name, COUNT(bids.item_id)
FROM items
LEFT JOIN bids
ON bids.item_id = items.id
GROUP BY items.id
ORDER BY items.id;