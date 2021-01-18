-- SELECT id, dt,
-- MAX(COALESCE("AverageTemperature", 0)) AS "MaxAverage", 
-- "AverageTemperatureUncertainty", "City", 
-- "Country", "Latitude", "Longitude"
-- FROM "Global_Land_Temperatures_By_City" 
-- WHERE extract(YEAR from "dt") >= 2000
-- GROUP BY "id", dt", "City", "AverageTemperatureUncertainty", 
-- "Country",  "Latitude", "Longitude"
-- ORDER BY "MaxAverage" DESC
-- LIMIT 1;

-- select * --count(*)
-- from "Global_Land_Temperatures_By_City"
-- limit 1;


-- SELECT *
-- FROM "Global_Land_Temperatures_By_City" 
-- WHERE "City" = 'Ahvaz'
-- ORDER BY "dt" DESC
-- LIMIT 100;


SELECT * --max(id) --8599212

FROM "Global_Land_Temperatures_By_City" 
WHERE id > 8599212
-- "City" = 'Ahvaz'
-- ORDER BY "dt" DESC
-- LIMIT 100;
