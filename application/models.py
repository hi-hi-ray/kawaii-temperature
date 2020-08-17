import peewee

db = peewee.SqliteDatabase('temp_database.db')


class BaseModel(peewee.Model):
    class Meta:
        database = db


class Temperature(BaseModel):
    id = peewee.IntegerField(unique=True, index=True, primary_key=True)
    sensor_humidity = peewee.IntegerField(null=True)
    sensor_temperature = peewee.IntegerField(null=True)
    type_of_request = peewee.CharField(null=True)
    wind_chill = peewee.CharField(null=True)
    timestamp = peewee.CharField(null=True)


if __name__ == '__main__':
    try:
        Temperature.create_table()
        print("Tabela 'Temperature' criada com sucesso!")
    except peewee.OperationalError:
        print("Tabela 'Temperature' já existe!")