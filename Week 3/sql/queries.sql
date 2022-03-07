--Grouping Sets Query
select 
    b.country,
    c.category,
    SUM(a.amount) as totalsales
from FACTSALES as a
left join DIMCOUNTRY as b
on a.countryid = b.countryid
left join DIMCATEGORY as c
on a.categoryid = c.categoryid
group by grouping sets(b.country, c.category, a.amount)
order by SUM(a.amount) desc;

--Rollup Query
select 
	b.year,
	c.country,
	SUM(a.amount) as totalsales
from FACTSALES as a
left join DIMDATE as b
on a.dateid = b.dateid
left join DIMCOUNTRY as c
on a.countryid = c.countryid
group by rollup(b.year, c.country, a.amount)
order by b.year, SUM(a.amount) desc;

--Cube Query
select 
	b.year,
	c.country,
	AVG(a.amount) as totalsales
from FACTSALES as a
left join DIMDATE as b
on a.dateid = b.dateid
left join DIMCOUNTRY as c
on a.countryid = c.countryid
group by cube(b.year, c.country, a.amount)
order by b.year, AVG(a.amount) desc;

--Materialized Query Table (MQT)
CREATE TABLE total_sales_per_country (country, total_sales) AS
(select 
	b.country,
	SUM(a.amount) as total_sales
from FACTSALES as a
left join DIMCOUNTRY as b
on a.countryid = b.countryid
group by b.country)
DATA INITIALLY DEFERRED REFRESH DEFERRED;

REFRESH TABLE total_sales_per_country;