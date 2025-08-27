# Architektur Template – StreamHive

Dieses Dokument beschreibt die **Systemarchitektur** des Projekts **StreamHive**. Es dient als Leitfaden für Entwickler, DevOps und Designer.

---

## 1. Projektübersicht
**Projektname:** StreamHive  
**Ziel:** Mini-YouTube-Clone, Plattform für Video-Upload, Streaming, Playlists und User-Interaktion.  
**Zielgruppe:** Nutzer, die Videos ansehen, hochladen und verwalten möchten.

---

## 2. Systemübersicht

| Layer | Technologie |
|-------|------------|
| Frontend | Angular / React |
| API Gateway | REST / GraphQL |
| Backend Services | C# .NET Core |
| Databases | PostgreSQL / MongoDB / RavenDB |


---

## 3. Microservices
| Service | Verantwortung | Datenbank |
|---------|---------------|-----------|
| Auth Service | User-Registrierung, Login, JWT-Token | PostgreSQL |
| Video Service | Upload, Streaming, Thumbnails | MongoDB |
| Playlist Service | Playlist-Management | PostgreSQL |
| Comment Service | Kommentare, Likes | MongoDB |
| Admin Service | Moderation, Analytics | RavenDB |

---

## 4. DevOps / Deployment
- **Containerization:** Docker für Backend & Frontend  
- **Orchestration:** Kubernetes / OpenShift  
- **CI/CD:** GitHub Actions Pipeline  
  - Lint & Test → Build → Deploy auf Staging → Test → Deploy Production  

---

## 5. Datenfluss / User Flow
1. **Video Upload:**  
   Frontend → API Gateway → Video Service → Speicherung in MongoDB → CDN-Verteilung
2. **Video Wiedergabe:**  
   Frontend → API Gateway → Video Service → Streaming → Player  
3. **User Management:**  
   Admin Frontend → API Gateway → Auth Service → PostgreSQL  

---

## 6. Sicherheitsarchitektur
- JWT-Authentifizierung für alle API Calls  
- HTTPS / TLS verschlüsselt  
- Role-Based Access Control (RBAC) für Admin Frontend  
- Datenbank-Zugriffe nur über Services  

---

## 7. Architekturprinzipien
- **Domain Driven Design (DDD)**: Microservices spiegeln Domains wider  
- **Test Driven Development (TDD)**: Unit- & Integrationstests  
- **Scalability & Flexibility**: Microservices, Container & Cloud Deployment  
- **Workflow Engine:** Camunda für komplexe Prozesse (z. B. Video-Moderation)  

