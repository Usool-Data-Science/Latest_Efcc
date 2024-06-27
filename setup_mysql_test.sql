-- srcipt that prepare a MySQL server
CREATE DATABASE IF NOT EXISTS efcc_db;
CREATE USER IF NOT EXISTS 'efcc'@'localhost' IDENTIFIED BY 'paswodEFCC1_346_810_trewq';
GRANT ALL PRIVILEGES ON efcc_db . * TO 'efcc_db'@'localhost';
GRANT SELECT ON performance_schema . * TO 'efcc_db'@'localhost';
