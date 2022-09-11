<script>
	import Button from '$lib/button.svelte';
    import Selection from "$lib/selection.svelte";
    import Input from '$lib/input.svelte';

    const items = [
        'route-1',
        'route-2',
        'route-3'
    ]
</script>

<form class="mt-8 space-y-6">
    <input type="hidden" name="remember" value="true" />
    <div class="rounded-md shadow-sm -space-y-px">
        <Selection name="Route" items={items}/>
        <Input name="Start Location" type="text"/>
        <Input name="Start Lattitude" type="text"/>
        <Input name="Start Longitude" type="number"/>
        <Input name="Start Time" type="time"/>
    </div>    
    <div class="pb-10 flex justify-around">
        <Button text="Close"/>
        <Button text="Update"/>
    </div>
</form>