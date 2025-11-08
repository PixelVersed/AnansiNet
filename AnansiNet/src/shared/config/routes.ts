import Gauge from "@lucide/svelte/icons/gauge";
import SettingsIcon from "@lucide/svelte/icons/settings";

export const routes = [
  {
    title: "Network Limiter",
    url: "/",
    icon: Gauge,
  },
  {
    title: "Settings",
    url: "/settings",
    icon: SettingsIcon,
  },
] as const;

export function getPageTitle(pathname: string): string {
  return routes.find(route => route.url === pathname)?.title || "Network Limiter";
}