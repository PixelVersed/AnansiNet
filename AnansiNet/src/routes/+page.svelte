<script lang="ts">
  // Components
  import { Input } from "$shared/components/ui/input/index.js";
  import { Button } from "$shared/components/ui/button/index.js";
  import { Checkbox } from "$shared/components/ui/checkbox/index.js";
  import * as Table from "$shared/components/ui/table/index.js";
  import * as ButtonGroup from "$shared/components/ui/button-group/index.js";

  // Icons
  import Stop from "@lucide/svelte/icons/circle-x";
  import Gauge from "@lucide/svelte/icons/gauge";
  import Search from "@lucide/svelte/icons/search";
  import Reset from "@lucide/svelte/icons/rotate-ccw";

  // Type
  type Device = {
    ip: string;
    mac: string;
    name: string;
    currentDownload: number;
    currentUpload: number;
    downloadCap: number;
    uploadCap: number;
    block: boolean;
    online: boolean;
  };

  type Host = {
    ip: string;
    mac: string;
    name: string;
    spoofed: boolean;
    limited: boolean;
    blocked: boolean;
  };

  // Input handlers
  // function handleInput(
  //   index: string,
  //   field: "downloadCap" | "uploadCap",
  //   value: number,
  // ) {
  //   devicess[index].field = value;
  // }

  // function handleBlockToggle(index: string, checked: boolean) {
  //   devicess[index].block = checked;
  //   devices = [...devices];
  // }

  import { pyInvoke } from "tauri-plugin-pytauri-api";
  type Dict<T> = Record<string, T>;

  async function get_connected_devices() {
    const hosts = await pyInvoke<Host[]>("get_hosts");
    map_hosts_to_devices(hosts);
  }
  let devices = $state<Dict<Device>>({});

  function map_hosts_to_devices(hosts: Host[]) {
    hosts.forEach((host) => {
      devices[host.ip] ??=  {
        ip: host.ip,
        mac: host.mac,
        block: false,
        online: true
      } as Device;
    });
  }
</script>

<section class="p-4 2xl:p-6">
  <!-- Toolbar -->
  <ButtonGroup.Root class="flex w-full items-center gap-2 py-2">
    <ButtonGroup.Root>
      <Button
        variant="outline"
        aria-label="Search"
        onclick={get_connected_devices}><Search />Search</Button
      >
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
      {#each Object.entries(devices) as [ip, device] (ip)}
        <Table.Row>
          <Table.Cell class="font-medium">{device.name}</Table.Cell>
          <Table.Cell class="font-medium">{device.ip}</Table.Cell>
          <Table.Cell class="font-medium">{device.mac}</Table.Cell>
          <Table.Cell class="font-medium">
            {device.currentDownload}<span class="text-xs text-muted-foreground px-1"
              >KB/s</span
            >
          </Table.Cell>
          <Table.Cell class="font-medium">
            {device.currentUpload}<span class="text-xs text-muted-foreground px-1"
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
              />
              <!-- oninput={(e) =>
                handleInput(ip, "downloadCap", Number(e.currentTarget.value))} -->
          </Table.Cell>

          <!-- Upload Cap Input -->
          <Table.Cell class="w-[130px]">
            <Input
              type="number"
              min="0"
              placeholder="KB/s"
              class="h-8 text-sm placeholder:text-xs"
              value={device.uploadCap}
              />
              <!-- oninput={(e) =>
                handleInput(ip, "uploadCap", Number(e.currentTarget.value))} -->
          </Table.Cell>

          <!-- Block Checkbox -->
          <Table.Cell class="text-center">
            <Checkbox
              bind:checked={device.block}
              />
              <!-- onchange={() => handleBlockToggle(ip, device.block)} -->
          </Table.Cell>
        </Table.Row>
      {/each}
    </Table.Body>
  </Table.Root>
</section>
