DROP TABLE IF EXISTS tracked_flights;
DROP TABLE IF EXISTS user_details;

CREATE TABLE tracked_flights (
  email TEXT UNIQUE NOT NULL,
  aircraft TEXT NOT NULL,
  carrier TEXT NOT NULL,
  date_and_time TEXT NOT NULL,
  PRIMARY KEY(email, aircraft, carrier, date_and_time),
  FOREIGN KEY (email) REFERENCES user_details (email)
);

CREATE TABLE user_details (
  email TEXT NOT NULL PRIMARY KEY,
  gen_code TEXT UNIQUE NOT NULL
);
