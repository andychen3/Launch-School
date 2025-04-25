SELECT items.name as "Bid on Items" FROM items WHERE items.id IN 
(SELECT item_id FROM bids);