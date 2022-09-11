<script>
    import Button from "../../../lib/button.svelte";
    import { writable } from 'svelte/store';
    import Modal from 'svelte-simple-modal';
    import Update from './update.svelte';
    import Add from "./add.svelte";
    const updateModal = writable(null);
    const addModal = writable(null);
const buses = [
    {
        License: "xyz",
        Code: "MMM",
        Capacity: 40,
        Driver: "MD. Abdul Kuddus",
        Contact: "+8801010101010",
        Active: true
    },
    {
        License: "xyz",
        Code: "MMM",
        Capacity: 40,
        Driver: "MD. Abdul Kuddus",
        Contact: "+8801010101010",
        Active: true
    },
    {
        License: "xyz",
        Code: "MMM",
        Capacity: 40,
        Driver: "MD. Abdul Kuddus",
        Contact: "+8801010101010",
        Active: true
    },
    {
        License: "xyz",
        Code: "MMM",
        Capacity: 40,
        Driver: "MD. Abdul Kuddus",
        Contact: "+8801010101010",
        Active: true
    },
    {
        License: "xyz",
        Code: "MMM",
        Capacity: 40,
        Driver: "MD. Abdul Kuddus",
        Contact: "+8801010101010",
        Active: true
    },
    {
        License: "xyz",
        Code: "MMM",
        Capacity: 40,
        Driver: "MD. Abdul Kuddus",
        Contact: "+8801010101010",
        Active: true
    },
    {
        License: "xyz",
        Code: "MMM",
        Capacity: 40,
        Driver: "MD. Abdul Kuddus",
        Contact: "+8801010101010",
        Active: true
    },
    {
        License: "xyz",
        Code: "MMM",
        Capacity: 40,
        Driver: "MD. Abdul Kuddus",
        Contact: "+8801010101010",
        Active: true
    },
]

</script>
<div class="w-full pl-3">
    <div class="w-full flex justify-between my-4">
        <div class="text-2xl">
            List of available buses
        </div>
        <div class="flex">
            <div class="mx-4">
                <Modal show={$updateModal}>
                    <Button onClick={() => updateModal.set(Update)} text="Update existing"/>
                </Modal>
            </div>
            <div>
                <Modal show={$addModal}>
                    <Button onClick={() => addModal.set(Add)} text="Add new bus"/>
                </Modal>
            </div>
        </div>
    </div>
    <div class="w-full grid grid-cols-12 gap-4 py-3 bg-gray-50 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
        <div class="col-span-2">
            License Number
        </div>
        <div class="col-span-1">
            Code
        </div>
        <div class="col-span-1">
            Capacity
        </div>
        <div class="col-span-3">
            Driver Name
        </div>
        <div class="col-span-3">
            Driver Contact Number
        </div>
        <div class="col-span-1">
            Is Active
        </div>
    </div>
    {#each buses as bus}
    <div class="w-full grid grid-cols-12 gap-4 py-3 text-left text-xs font-medium tracking-wider border-b-2">
        <div class="col-span-2">
            {bus.License}
        </div>
        <div class="col-span-1">
            {bus.Code}
        </div>
        <div class="col-span-1">
            {bus.Capacity}
        </div>
        <div class="col-span-3">
            {bus.Driver}
        </div>
        <div class="col-span-3">
            {bus.Contact}
        </div>
        <div class="col-span-1">
            {bus.Active}
        </div>
    </div>
    {/each}
</div>