# UI / UX Template – StreamHive

Dieses Dokument dient als Leitfaden für die Gestaltung der Benutzeroberfläche und Nutzererfahrung des Projekts **StreamHive**.

---

## 1. Projektübersicht
**Projektname:** StreamHive  
**Ziel:** Mini-YouTube-Clone, Plattform für Video-Upload, Streaming, Playlists und User-Interaktion.  
**Zielgruppe:** Nutzer, die Videos ansehen, hochladen und verwalten möchten.

---

## 2. Designprinzipien
- **Klarheit:** Alle Interfaces müssen intuitiv verständlich sein.  
- **Konsistenz:** Wiederkehrende Komponenten (Buttons, Forms, Cards) einheitlich gestalten.  
- **Responsiveness:** Mobile, Tablet und Desktop unterstützen.  
- **Zugänglichkeit (Accessibility):** ARIA-Labels, Farbkontraste > 4.5:1.

---

## 3. Farbpalette
| Farbe | HEX | Verwendung |
|-------|-----|------------|
| Primär | #1E88E5 | Hauptaktionen, Links, Buttons |
| Sekundär | #FFC107 | Akzente, Highlights |
| Hintergrund | #F5F5F5 | Seitenhintergrund |
| Text | #212121 | Primärer Text |
| Text Sekundär | #757575 | Untertitel, Hinweise |

---

## 4. Typografie
| Element | Schriftart | Gewicht | Größe |
|---------|------------|--------|------|
| H1 | Roboto | Bold | 32px |
| H2 | Roboto | Medium | 24px |
| H3 | Roboto | Medium | 20px |
| Body | Roboto | Regular | 16px |
| Caption | Roboto | Regular | 14px |

---

## 5. Komponenten
### 5.1 Buttons
- Primär: `bg-primary text-white rounded px-4 py-2`  
- Sekundär: `bg-secondary text-black rounded px-4 py-2`  
- Zustände: hover, active, disabled  

### 5.2 Forms / Inputs
- Input-Felder mit Label über dem Feld  
- Error-States rot (#D32F2F)  
- Placeholder-Farbe: #9E9E9E  

### 5.3 Cards (Video Previews)
- Thumbnail oben  
- Titel + Beschreibung darunter  
- Action-Buttons: Like, Share, Add to Playlist  

---

## 6. Layout / Grid
- **Desktop:** 12-Spalten Grid  
- **Tablet:** 8-Spalten Grid  
- **Mobile:** 4-Spalten Grid  
- Abstand zwischen Komponenten: 16px (Standard Padding / Margin)  

---

## 7. Navigation
- **Topbar:** Logo links, Searchbar, User-Avatar rechts  
- **Sidebar (optional Admin):** Vertikale Menüleiste mit Icons + Text  

---

## 8. Wireframes / Mockups
> **Hinweis:** Alle Screens müssen als Figma-Dateien gepflegt werden.  
- `Home`: Video-Feed, Trending, Kategorien  
- `Video-Detail`: Player, Titel, Beschreibung, Kommentare, Actions  
- `Upload`: Upload-Form, Thumbnail-Preview, Kategorien  
- `Profile`: User-Videos, Playlists, Einstellungen  
- `Admin`: Dashboard, User-Management, Video-Moderation  

---

## 9. User Flow Beispiele
1. **Video Upload**
   - User klickt „Upload“ → Upload-Form öffnet sich → Datei wählen → Metadaten eingeben → Submit → Video wird verarbeitet → Erfolgs-Message
2. **Video anschauen**
   - User klickt Video → Player öffnet → Vorschläge rechts → Kommentare und Like-Buttons verfügbar  

