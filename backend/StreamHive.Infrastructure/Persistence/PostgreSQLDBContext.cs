using Npgsql;
using System.Data;
using System.Diagnostics;

namespace StreamHive.Infrastructure.Persistence
{
    public class PostgresDbContext
    {
        private readonly string _connectionString;
        private readonly NpgsqlConnection _connection;

        public PostgresDbContext(string connectionString)
        {
            _connectionString = connectionString;
            _connection = new NpgsqlConnection(_connectionString);

            try
            {
                _connection.Open();
                using var cmd = new NpgsqlCommand("SELECT version();", _connection);
                var version = cmd.ExecuteScalar()?.ToString();
                Debug.WriteLine($"✅ Verbindung zu PostgreSQL hergestellt! Version: {version}");
            }
            catch (Exception ex)
            {
                Debug.WriteLine($"❌ Verbindung zu PostgreSQL fehlgeschlagen: {ex.Message}");
                throw;
            }
            finally
            {
                _connection.Close();
            }
        }

        // Zugriffsmethode für Queries
        public IDbConnection CreateConnection()
        {
            return new NpgsqlConnection(_connectionString);
        }
    }
}
