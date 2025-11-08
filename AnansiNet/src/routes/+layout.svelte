<script lang="ts">
  import "../app.css";
  import { onMount } from "svelte";

  // Components
  import { ModeWatcher, setMode } from "mode-watcher";
  import * as Sidebar from "$shared/components/ui/sidebar/index.js";
  import AppSidebar from "$shared/components/navigation/app-sidebar.svelte";
  import AppHeader from "$shared/components/navigation/app-header.svelte";

  let { children } = $props();

  onMount(() => {
    setMode("dark");
  });
</script>

<ModeWatcher track={false} />
<Sidebar.Provider>
  <AppSidebar />
  <main class="w-full h-full">
    <AppHeader />
    {@render children?.()}
  </main>
</Sidebar.Provider>