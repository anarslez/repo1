/*select * from countrylanguage 
where Language = 'Slovene'
order by percentage;
*/
/*SELECT country.name AS country, COUNT(city.id) AS number_cities
FROM country
JOIN city ON country.code = city.countrycode
GROUP BY country.code
ORDER BY COUNT(city.id) desc
*/
/*select * from country 
join city on country.code = city.countrycode
where country.Name = 'mexico'
GROUP BY city.id HAVING city.population > 500000;
*/
/*select * from country 
join countrylanguage on country.code = countrylanguage.countrycode
GROUP BY countrylanguage.Language HAVING countrylanguage.Percentage > 89
ORDER BY countrylanguage.percentage desc;
*/
/*select Name, SurfaceArea, Population from country
where population > 10000 and surfacearea < 501
ORDER BY population desc;*/
/*SELECT name, governmentform, capital, LifeExpectancy
FROM country 
WHERE governmentform = 'Constitutional Monarchy' and capital > 200 and lifeexpectancy > 75*/
/*select * from country 
join city on country.code = city.countrycode
where country.Name = 'argentina'
GROUP BY city.id HAVING city.District = 'buenos aires' and city.Population > 50000;*/
/*SELECT country.region, COUNT(country.Code) AS number_countries
FROM country
GROUP BY region */

