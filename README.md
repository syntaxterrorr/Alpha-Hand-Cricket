# Alpha-Hand-Cricket
A hand cricket game bot using reinforcement learning. Final year project for B.E. (Engineering).

Fortnightly reports: https://docs.google.com/spreadsheets/d/1TMdjrsPuM0FtMCsIjYVejufDfuTNtKeGaQPBF9INE4A/edit?usp=sharing

White book: https://drive.google.com/file/d/1-QFvDTL7rCVm590t0Uq06CQhM2Txg6S0/view?usp=sharing

### Database Setup
1. Create database
```
$ mysql -u <username> -p <password>
mysql> CREATE DATABASE alpha_hand_cricket
```
2. Import database schema
```
$ mysql -u <username> -p <password> alpha_hand_cricket < sql/ddl.sql`
```
3. To include sample data (optional)
```
$ mysql -u <username> -p <password> yourdatabase < sql/sample_dml.sql`
```
### Play Game
```
$ python alpha_hand_cricket.py
```
