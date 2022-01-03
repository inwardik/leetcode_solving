# Write your MySQL query statement below
SELECT email
FROM   Person
GROUP  BY email
HAVING Count(email) > 1;

--

select Email from
(
  select Email, count(Email) as num
  from Person
  group by Email
) as statistic
where num > 1
;