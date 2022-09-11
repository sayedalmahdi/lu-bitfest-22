<script>
	import Button from '$lib/button.svelte';
    import { writable } from 'svelte/store';
    import Modal from 'svelte-simple-modal';
    import Update from './update.svelte';
    import Add from "./add.svelte";
    const updateModal = writable(null);
    const addModal = writable(null);

    const routes = [
        {
            id: '1',
            "start location": "Modina Market",
            "start lattitude": "x",
            "start longitude": "y",
            "start time": "5 AM"
        },
        {
            id: '1',
            "start location": "Modina Market",
            "start lattitude": "x",
            "start longitude": "y",
            "start time": "5 AM"
        },
        {
            id: '1',
            "start location": "Modina Market",
            "start lattitude": "x",
            "start longitude": "y",
            "start time": "5 AM"
        },
        {
            id: '1',
            "start location": "Modina Market",
            "start lattitude": "x",
            "start longitude": "y",
            "start time": "5 AM"
        },
        {
            id: '1',
            "start location": "Modina Market",
            "start lattitude": "x",
            "start longitude": "y",
            "start time": "5 AM"
        },
        {
            id: '1',
            "start location": "Modina Market",
            "start lattitude": "x",
            "start longitude": "y",
            "start time": "5 AM"
        },
        {
            id: '1',
            "start location": "Modina Market",
            "start lattitude": "x",
            "start longitude": "y",
            "start time": "5 AM"
        },
    ]

</script>
<div class="w-full pl-3">
    <div class="w-full flex justify-between my-4">
        <div class="text-2xl">
            List of available routes
        </div>
        <div class="flex">
            <div class="mx-4">
                <Modal show={$updateModal}>
                    <Button onClick={() => updateModal.set(Update)} text="Update existing"/>
                </Modal>
            </div>
            <div>
                <Modal show={$addModal}>
                    <Button onClick={() => addModal.set(Add)} text="Add new route"/>
                </Modal>
            </div>
        </div>
    </div>
    <div class="w-full grid grid-cols-3 gap-4 py-3 bg-gray-50 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
        <div class="col-span-1">
            Route Number
        </div>
        <div class="col-span-1">
            Start Location
        </div>
        <div class="col-span-1">
            Start Time
        </div>
    </div>
    {#each routes as route}
    <div class="w-full grid grid-cols-3 gap-4 py-3 text-left text-xs font-medium tracking-wider border-b-2">
        <div class="col-span-1">
            {route.id}
        </div>
        <div class="col-span-1">
            {route["start location"]}
        </div>
        <div class="col-span-1">
            {route["start time"]}
        </div>
    </div>
    {/each}
</div>