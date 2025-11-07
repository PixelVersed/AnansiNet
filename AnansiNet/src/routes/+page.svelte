<script lang="ts">
  // Components
  import { Input } from "$lib/components/ui/input/index.js";
  import { Button } from "$lib/components/ui/button/index.js";
  import { Checkbox } from "$lib/components/ui/checkbox/index.js";
  import * as Table from "$lib/components/ui/table/index.js";
  import * as ButtonGroup from "$lib/components/ui/button-group/index.js";

  // Icons
  import Stop from "@lucide/svelte/icons/circle-x";
  import Gauge from "@lucide/svelte/icons/gauge";
  import Search from "@lucide/svelte/icons/search";
  import Reset from "@lucide/svelte/icons/rotate-ccw";

  // Type
  type Device = {
    name: string;
    ip: string;
    mac: string;
    download: string;
    upload: string;
    downloadCap: string;
    uploadCap: string;
    block: boolean;
  };

  // Example device list (for table preview only)
  let devices = $state<Device[]>([
    {
      name: "Your PC",
      ip: "192.168.1.99",
      mac: "EB98329DS89",
      download: "2000",
      upload: "1000",
      downloadCap: "1500",
      uploadCap: "500",
      block: false,
    },
    {
      name: "192.168.1.100",
      ip: "192.168.1.100",
      mac: "CC68329FS12",
      download: "2000",
      upload: "1000",
      downloadCap: "",
      uploadCap: "",
      block: true,
    },
  ]);

  // Input handlers
  function handleInput(
    index: number,
    field: "downloadCap" | "uploadCap",
    value: string
  ) {
    devices[index][field] = value;
  }

  function handleBlockToggle(index: number, checked: boolean) {
    devices[index].block = checked;
    devices = [...devices];
  }

</script>

<section class="p-4 2xl:p-6">
  <!-- Toolbar -->
  <ButtonGroup.Root class="flex w-full items-center gap-2 py-2">
    <ButtonGroup.Root>
      <Button variant="outline" aria-label="Search"><Search />Search</Button>
    </ButtonGroup.Root>
    <ButtonGroup.Root>
      <Button variant="outline" aria-label="Apply">
        <Gauge />Apply
      </Button>
      <Button variant="outline" aria-label="Stop"><Stop />Stop</Button>
    </ButtonGroup.Root>
    <ButtonGroup.Root class="ml-auto">
      <Button variant="outline" size="icon" aria-label="Reset">
        <Reset />
      </Button>
    </ButtonGroup.Root>
  </ButtonGroup.Root>

  <!-- Table -->
  <Table.Root>
    <Table.Caption>A list of discovered devices.</Table.Caption>
    <Table.Header>
      <Table.Row>
        <Table.Head>Name</Table.Head>
        <Table.Head>IP</Table.Head>
        <Table.Head>Mac</Table.Head>
        <Table.Head>Download</Table.Head>
        <Table.Head>Upload</Table.Head>
        <Table.Head>Download Cap</Table.Head>
        <Table.Head>Upload Cap</Table.Head>
        <Table.Head>Block</Table.Head>
      </Table.Row>
    </Table.Header>
    <Table.Body>
      {#each devices as device, i (device.mac)}
        <Table.Row>
          <Table.Cell class="font-medium">{device.name}</Table.Cell>
          <Table.Cell class="font-medium">{device.ip}</Table.Cell>
          <Table.Cell class="font-medium">{device.mac}</Table.Cell>
          <Table.Cell class="font-medium">
            {device.download}<span class="text-xs text-muted-foreground px-1"
              >KB/s</span
            >
          </Table.Cell>
          <Table.Cell class="font-medium">
            {device.upload}<span class="text-xs text-muted-foreground px-1"
              >KB/s</span
            >
          </Table.Cell>

          <!-- Download Cap Input -->
          <Table.Cell class="w-[130px]">
            <Input
              type="number"
              min="0"
              placeholder="KB/s"
              class="h-8 text-sm placeholder:text-xs"
              value={device.downloadCap}
              oninput={(e) =>
                handleInput(i, "downloadCap", e.currentTarget.value)}
            />
          </Table.Cell>

          <!-- Upload Cap Input -->
          <Table.Cell class="w-[130px]">
            <Input
              type="number"
              min="0"
              placeholder="KB/s"
              class="h-8 text-sm placeholder:text-xs"
              value={device.uploadCap}
              oninput={(e) =>
                handleInput(i, "uploadCap", e.currentTarget.value)}
            />
          </Table.Cell>

          <!-- Block Checkbox -->
          <Table.Cell class="text-center">
           <Checkbox bind:checked={device.block} onchange={() => handleBlockToggle(i, device.block)} />
          </Table.Cell>
        </Table.Row>
      {/each}
    </Table.Body>
  </Table.Root>
</section>
