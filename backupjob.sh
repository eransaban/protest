sudo mysqldump --opt prac > /tmp/backup/prac-$(date).sql
aws s3 sync /tmp/backup s3://saban-sql-backup/backup
