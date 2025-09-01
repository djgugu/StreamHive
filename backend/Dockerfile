FROM mcr.microsoft.com/dotnet/sdk:7.0 AS build
WORKDIR /app

COPY *.sln .
COPY StreamHive.API/*.csproj ./StreamHive.API/
COPY StreamHive.Core/*.csproj ./StreamHive.Core/
COPY StreamHive.Infrastructure/*.csproj ./StreamHive.Infrastructure/
RUN dotnet restore

COPY . .
WORKDIR /app/StreamHive.API
RUN dotnet publish -c Release -o out

FROM mcr.microsoft.com/dotnet/aspnet:7.0
WORKDIR /app
COPY --from=build /app/StreamHive.API/out .
ENTRYPOINT ["dotnet", "StreamHive.API.dll"]
