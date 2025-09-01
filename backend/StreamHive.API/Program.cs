using Microsoft.AspNetCore.Builder;
using StreamHive.Infrastructure.Persistence;
using System.Diagnostics;

var builder = WebApplication.CreateBuilder(args);

// Mongo Settings laden
var mongoSettings = builder.Configuration.GetSection("MongoDbSettings");
var connectionString = mongoSettings["ConnectionString"];
var databaseName = mongoSettings["DatabaseName"];

// DbContext registrieren

// MongoDB
builder.Services.AddSingleton(new MongoDbContext(connectionString, databaseName));

// PostgreSQL
/*var postgresConnection = builder.Configuration.GetConnectionString("PostgresConnection");
builder.Services.AddSingleton(new PostgresDbContext(postgresConnection));*/
builder.Services.AddScoped<PostgresDbContext>(provider =>
    new PostgresDbContext(postgresConnection));

// Add services to the container.
// init Swagger (OpenAPI) 
builder.Services.AddOpenApi();
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();


var app = builder.Build();

Debug.WriteLine("Hello World");
// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
    app.MapOpenApi();
}

app.UseHttpsRedirection();

var summaries = new[]
{
    "Freezing", "Bracing", "Chilly", "Cool", "Mild", "Warm", "Balmy", "Hot", "Sweltering", "Scorching"
};

app.MapGet("/weatherforecast", () =>
{
    var forecast = Enumerable.Range(1, 5).Select(index =>
        new WeatherForecast
        (
            DateOnly.FromDateTime(DateTime.Now.AddDays(index)),
            Random.Shared.Next(-20, 55),
            summaries[Random.Shared.Next(summaries.Length)]
        ))
        .ToArray();
    return forecast;
})
.WithName("GetWeatherForecast");

app.MapGet("/getPerson", () =>
{
    var person = new Person("Max Mustermann", 30, new string[] { "Lesen", "Wandern" });
    return person;
})
.WithName("getPerson");



app.Run();

record WeatherForecast(DateOnly Date, int TemperatureC, string? Summary)
{
    public int TemperatureF => 32 + (int)(TemperatureC / 0.5556);
}
record Person(string Name, int Age, string[] Hobbies);

