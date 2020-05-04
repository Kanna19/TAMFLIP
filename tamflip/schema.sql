DROP TABLE IF EXISTS tracked_flights;
DROP TABLE IF EXISTS user_details;

PRAGMA foreign_keys = ON;

CREATE TABLE user_details (
  email TEXT NOT NULL PRIMARY KEY,
  gen_code TEXT UNIQUE NOT NULL
);

CREATE TABLE tracked_flights (
  email TEXT UNIQUE NOT NULL,
  aircraft TEXT NOT NULL,
  carrier TEXT NOT NULL,
  date_and_time TEXT NOT NULL,
  prev_price TEXT NOT NULL,
  PRIMARY KEY(email, aircraft, carrier, date_and_time),
  FOREIGN KEY (email) REFERENCES user_details (email)
);

INSERT INTO user_details VALUES ("flightapi@yandex.com", "prothin");
INSERT INTO user_details VALUES ("chaitu7261998@gmail.com", "prokc");
INSERT INTO user_details VALUES ("kannasasuke19@gmail.com", "bot");

INSERT INTO tracked_flights VALUES ("flightapi@yandex.com", "DH8", "H1", "2020-05-12T11:10:00", "15832.00");
INSERT INTO tracked_flights VALUES ("chaitu7261998@gmail.com", "DH8", "H1", "2020-05-12T11:10:00", "15832.00");
INSERT INTO tracked_flights VALUES ("kannasasuke19@gmail.com", "DH8", "H1", "2020-05-12T11:10:00", "15832.00");
