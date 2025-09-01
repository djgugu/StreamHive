import type { Routes } from "@angular/router";
import { HomePageComponent } from "./pages/home-page/home-page.component";
import { VideoDetailPageComponent } from "./pages/video-detail-page/video-detail-page.component";
import { UploadPageComponent } from "./pages/upload-page/upload-page.component";
import { ChannelPageComponent } from "./pages/channel-page/channel-page.component";
import { SearchPageComponent } from "./pages/search-page/search-page.component";
import { LoginPageComponent } from "./pages/login-page/login-page.component";
import { AdminDashboardComponent } from "./pages/admin-dashboard/admin-dashboard.component";
import { NotFoundPageComponent } from "./pages/not-found-page/not-found-page.component";

export const routes: Routes = [
  { path: "", component: HomePageComponent },
  { path: "video/:id", component: VideoDetailPageComponent },
  { path: "upload", component: UploadPageComponent },
  { path: "channel/:id", component: ChannelPageComponent },
  { path: "search", component: SearchPageComponent },
  { path: "login", component: LoginPageComponent },
  { path: "admin", component: AdminDashboardComponent },
  { path: "**", component: NotFoundPageComponent }
];
