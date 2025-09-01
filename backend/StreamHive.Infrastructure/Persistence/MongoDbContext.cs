using MongoDB.Bson;
using MongoDB.Driver;
using System.Diagnostics;

namespace StreamHive.Infrastructure.Persistence
{
    public class MongoDbContext
    {
        private readonly IMongoDatabase _database;
        private readonly MongoClient _client;

        public MongoDbContext(string connectionString, string databaseName)
        {
            _client = new MongoClient(connectionString);
            _database = _client.GetDatabase(databaseName);
            // Test: Ping an MongoDB
            var command = new BsonDocument("ping", 1);
            _database.RunCommand<BsonDocument>(command);
            Debug.WriteLine("✅ Verbindung zu MongoDB hergestellt!");
        }

        public object Database { get; set; }

        // Beispiel: Zugriff auf eine Collection
        public IMongoCollection<T> GetCollection<T>(string name)
        {
            return _database.GetCollection<T>(name);
        }
    }
}
