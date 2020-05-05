DROP TABLE IF EXISTS tracked_flights;
DROP TABLE IF EXISTS user_details;

PRAGMA foreign_keys = ON;

CREATE TABLE user_details (
  email TEXT NOT NULL PRIMARY KEY,
  gen_code TEXT UNIQUE NOT NULL
);

CREATE TABLE tracked_flights (
  email TEXT UNIQUE NOT NULL,
  aircraft_code TEXT NOT NULL,
  carrier_code TEXT NOT NULL,
  adults TEXT NOT NULL,
  children TEXT NOT NULL,
  infants TEXT NOT NULL,
  from_location TEXT NOT NULL,
  to_location TEXT NOT NULL,
  departure_date TEXT NOT NULL,
  return_date TEXT,
  type_of_class TEXT NOT NULL,
  prev_price TEXT NOT NULL,
  PRIMARY KEY(email, aircraft_code, carrier_code, departure_date),
  FOREIGN KEY (email) REFERENCES user_details (email)
);

INSERT INTO user_details VALUES ("flightapi@yandex.com", "prothin");
INSERT INTO user_details VALUES ("chaitu7261998@gmail.com", "prokc");
INSERT INTO user_details VALUES ("kannasasuke19@gmail.com", "bot");

INSERT INTO tracked_flights VALUES ("chaitu7261998@gmail.com", "319", "AI", "1", "0", "0", "HYD", "BLR", "2020-05-22", "2020-05-27", "Business", "26674");
INSERT INTO tracked_flights VALUES ("kannasasuke19@gmail.com", "32B", "AI", "2", "1", "0", "HYD", "BLR", "2020-05-23", NULL, "Business", "37237");
