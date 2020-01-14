db.createCollection("temporaly_data_user")
db.TemporalyDataUser.createIndex( { "createdAt": 1 }, { expireAfterSeconds: 600 } )
db.TemporalyDataUser.createIndex( { "validationHashLink": 2 } )
