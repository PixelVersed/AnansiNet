<script lang="ts">
  import { page } from "$app/state";
  import { Button } from "$shared/components/ui/button/index.js";
  import { Separator } from "$shared/components/ui/separator/index.js";
  import * as Sidebar from "$shared/components/ui/sidebar/index.js";
  import { getPageTitle } from "$shared/config/routes";

  const currentPageTitle = $derived(getPageTitle(page.url.pathname));
</script>

<header class="py-1 2xl:py-2 border-b">
  <div class="flex w-full items-center gap-1 px-4 lg:gap-2 2xl:px-6">
    <Sidebar.Trigger class="-ml-1" />
    <Separator
      orientation="vertical"
      class="me-2 data-[orientation=vertical]:h-4"
    />
    <h1 class="text-base font-medium">{currentPageTitle}</h1>
    <div class="ml-auto flex items-center gap-2">
      <Button
        href="https://github.com/PixelVersed/AnansiNet"
        variant="ghost"
        size="sm"
        class="dark:text-foreground hidden sm:flex"
        target="_blank"
        rel="noopener noreferrer"
      >
        GitHub
      </Button>
    </div>
  </div>
</header>
