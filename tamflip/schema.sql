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
  from_location TEXT NOT NULL,
  to_location TEXT NOT NULL,
  departure_date TEXT NOT NULL,
  return_date TEXT, 
  type_of_class TEXT NOT NULL,
  prev_price TEXT NOT NULL,
  PRIMARY KEY(email, aircraft, carrier, departure_date),
  FOREIGN KEY (email) REFERENCES user_details (email)
);

INSERT INTO user_details VALUES ("flightapi@yandex.com", "prothin");
INSERT INTO user_details VALUES ("chaitu7261998@gmail.com", "prokc");
INSERT INTO user_details VALUES ("kannasasuke19@gmail.com", "bot");

INSERT INTO tracked_flights VALUES ("flightapi@yandex.com", "DH8", "H1","1","1","0", "HYD", "BLR", "2020-05-27", "2020-05-30", "Business",  "15832.00");
INSERT INTO tracked_flights VALUES ("chaitu7261998@gmail.com", "DH8", "H1","1","1","0", "HYD", "BLR", "2020-05-27", "2020-05-30", "Business",  "15832.00");
INSERT INTO tracked_flights VALUES ("kannasasuke19@gmail.com", "DH8", "H1","1","1","0", "HYD", "MAA", "2020-05-27", "2020-05-30", "Business",  "15832.00");