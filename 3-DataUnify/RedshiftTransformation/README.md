First Build Airflow Image locally
`docker-compose build`

Then config DBT profile for connecting to the Redshift.
```
cp .env.template .env
vim .env
```

Next, to deploy Airflow
`docker-compose up -d`

Rebuild Airflow Image
`docker-compose build`