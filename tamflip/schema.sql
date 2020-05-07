DROP TABLE IF EXISTS tracked_flights;

CREATE TABLE tracked_flights (
  id INTEGER PRIMARY KEY,
  email TEXT NOT NULL,
  dept_aircraft_code TEXT NOT NULL,
  dept_carrier_code TEXT NOT NULL,
  return_aircraft_code TEXT,
  return_carrier_code TEXT,
  adults TEXT NOT NULL,
  children TEXT NOT NULL,
  infants TEXT NOT NULL,
  from_location TEXT NOT NULL,
  to_location TEXT NOT NULL,
  departure_date TEXT NOT NULL,
  return_date TEXT,
  type_of_class TEXT NOT NULL,
  prev_price TEXT NOT NULL
);

INSERT INTO tracked_flights VALUES (NULL, "kannasasuke19@gmail.com", "319", "AI", "32B", "AI","2", "1", "0", "HYD", "BLR", "2020-05-22", "2020-05-27", "Business", "37220");
INSERT INTO tracked_flights VALUES (NULL, "chaitu7261998@gmail.com", "319", "AI","319", "AI", "1", "0", "0", "HYD", "BLR", "2020-05-22", "2020-05-27", "Business", "26674");
INSERT INTO tracked_flights VALUES (NULL, "re1nth98@gmail.com", "319", "AI", "32B", "AI","2", "1", "0", "HYD", "BLR", "2020-05-22", "2020-05-27", "Business", "37220");
INSERT INTO tracked_flights VALUES (NULL, "ramanudeepp@gmail.com", "319", "AI", "32B", "AI","2", "1", "0", "HYD", "BLR", "2020-05-22", "2020-05-27", "Business", "37220");
INSERT INTO tracked_flights VALUES (NULL, "kannasasuke19@gmail.com", "319", "AI", "32B", "AI","2", "1", "0", "HYD", "BLR", "2020-05-22", NULL, "Business", "37230");
INSERT INTO tracked_flights VALUES (NULL, "ramanudeepp@gmail.com", "738", "PC", NULL, NULL, "2", "1", "0", "AUH", "DOH", "2020-05-22", NULL, "Business", "80000");
INSERT INTO tracked_flights VALUES (NULL, "kannasasuke19@gmail.com", "738", "PC", NULL, NULL, "2", "1", "0", "AUH", "DOH", "2020-05-22", NULL, "Economy", "80000");
INSERT INTO tracked_flights VALUES (NULL, "chaitu7261998@gmail.com", "73H", "VA", "73W", "VA", "1", "0", "0", "NTL", "MEL", "2020-05-14", "2020-05-16", "Economy", "12848.00");
INSERT INTO tracked_flights VALUES (NULL, "re1nth98@gmail.com", "320", "JQ", "320", "JQ", "1", "0", "0", "NTL", "MEL", "2020-05-14", "2020-05-16", "Economy", "12878.00");
INSERT INTO tracked_flights VALUES (NULL, "chaitu7261998@gmail.com", "320", "F9", "320", "F9", "1", "0", "0", "LAX", "NYC", "2020-05-16", "2020-05-18", "Economy", "13904.00");
INSERT INTO tracked_flights VALUES (NULL, "re1nth98@gmail.com", "32B", "NK", "32A", "NK", "1", "0", "0", "LAX", "NYC", "2020-05-16", "2020-05-18", "Economy", "19299.00");
INSERT INTO tracked_flights VALUES (NULL, "ramanudeepp@gmail.com", "32B", "NK", "32A", "NK", "1", "0", "0", "LAX", "NYC", "2020-05-16", "2020-05-18", "Economy", "25854.00");
