--задание 1
SELECT c.login, COUNT(o.*) AS active_orders
FROM Couriers c
JOIN Orders o ON o.courierId = c.id
WHERE o.inDelivery = TRUE
GROUP BY c.login

--задание 2
SELECT o.track,
 CASE
  WHEN o.finished = true THEN '2'
  WHEN o.cancelled = true THEN '-1'
  WHEN o.inDelivery = true THEN '1'
  ELSE 0
 END AS status
FROM Orders o