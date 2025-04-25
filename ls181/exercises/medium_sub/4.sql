SELECT name FROM bidders
WHERE EXISTS (SELECT 1 FROM bids WHERE bidders.id = bids.bidder_id);

SELECT name
FROM bidders
INNER JOIN bids
ON bids.bidder_id = bidders.id
GROUP BY bidders.id
ORDER BY bidders.id;