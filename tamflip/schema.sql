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

INSERT INTO tracked_flights VALUES (NULL,"kannasasuke19@gmail.com", "319", "AI", "32B", "AI","2", "1", "0", "HYD", "BLR", "2020-05-22", "2020-05-27", "Business", "37237");
INSERT INTO tracked_flights VALUES (NULL,"chaitu7261998@gmail.com", "319", "AI","319", "AI", "1", "0", "0", "HYD", "BLR", "2020-05-22", "2020-05-27", "Business", "26674");
INSERT INTO tracked_flights VALUES (NULL,"re1nth98@gmail.com", "319", "AI", "32B", "AI","2", "1", "0", "HYD", "BLR", "2020-05-22", "2020-05-27", "Business", "37237");
INSERT INTO tracked_flights VALUES (NULL,"ramanudeepp@gmail.com", "319", "AI", "32B", "AI","2", "1", "0", "HYD", "BLR", "2020-05-22", "2020-05-27", "Business", "37237");
INSERT INTO tracked_flights VALUES (NULL,"dummyboi@dummyboi.com", "319", "AI", "32B", "AI","2", "1", "0", "HYD", "BLR", "2020-05-05", NULL, "Business", "37237");
INSERT INTO tracked_flights VALUES (NULL,"dummyboi@dummyboi.com", "319", "AI", "32B", "AI","2", "1", "0", "HYD", "BLR", "2020-05-03", "2020-05-05", "Business", "37237");
INSERT INTO tracked_flights VALUES (NULL,"dummyboi@dummyboi.com", "319", "AI", "32B", "AI","2", "1", "0", "HYD", "BLR", "2020-05-01", "2020-05-22", "Business", "37237");
INSERT INTO tracked_flights VALUES (NULL,"kannasasuke19@gmail.com", "319", "AI", "32B", "AI","2", "1", "0", "HYD", "BLR", "2020-05-22", NULL, "Business", "37237");
INSERT INTO tracked_flights VALUES (NULL,"ramanudeepp@gmail.com", "738", "PC", NULL, NULL, "2", "1", "0", "AUH", "DOH", "2020-05-22", NULL, "Business", "25000");
INSERT INTO tracked_flights VALUES (NULL,"kannasasuke19@gmail.com", "738", "PC", NULL, NULL, "2", "1", "0", "AUH", "DOH", "2020-05-22", NULL, "Economy", "25000")
