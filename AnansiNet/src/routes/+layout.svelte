<script lang="ts">
  import "../app.css";

  // Components
  import { ModeWatcher } from "mode-watcher";
  import * as Sidebar from "$lib/components/ui/sidebar/index.js";
  import AppSidebar from "$lib/components/navigation/app-sidebar.svelte";
  import AppHeader from "$lib/components/navigation/app-header.svelte";

  let { children } = $props();
</script>

<ModeWatcher />
<Sidebar.Provider>
  <AppSidebar />
  <main class="w-full h-full">
    <AppHeader />
    {@render children?.()}
  </main>
</Sidebar.Provider>
