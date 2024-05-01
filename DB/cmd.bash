## for login as user ram and db as inovicedb

psql -U ram invoicedb

## after login, to run script sql 

\i /path/to/script/file/tableCreation.sql

## to see all tables detail 

\dt 

## To drop any table 

drop table if exists "clientdetail" cascade;

