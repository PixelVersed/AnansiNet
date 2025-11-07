<script lang="ts">
  import "../app.css";

  // Components
  import { ModeWatcher } from "mode-watcher";
  import * as Sidebar from "$lib/components/ui/sidebar/index.js";
  import AppSidebar from "$lib/components/navigation/app-sidebar.svelte";

  let { children } = $props();
</script>

<ModeWatcher />
<Sidebar.Provider>
  <AppSidebar />
  <main>
    <Sidebar.Trigger />
    {@render children?.()}
  </main>
</Sidebar.Provider>
