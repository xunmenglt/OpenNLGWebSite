docker compose down
docker compose rm -f
docker compose build
docker compose up -d
docker exec -i dockerscript-mysql-1 mysql -h127.0.0.1 -uroot -popennlg opennlg < opennlg.sql