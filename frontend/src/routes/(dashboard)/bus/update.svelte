<script>
    import Input from "../../../lib/input.svelte";
    import Selection from "../../../lib/selection.svelte";
    import Button from "../../../lib/button.svelte";

    const items = [
        'bus-1',
        'bus-2',
        'bus-3'
    ]
</script>

<form class="mt-8 space-y-6">
    <input type="hidden" name="remember" value="true" />
    <div class="rounded-md shadow-sm -space-y-px">
        <Selection name="Buses" items={items}/>
        <Input name="License" type="text"/>
        <Input name="Code" type="text"/>
        <Input name="Capacity" type="number"/>
        <Input name="Driver Name" type="text"/>
        <Input name="Contact Number" type="tel"/>
        <div class="flex items-center">
            <Input name="Is Active" type="checkbox"/>
            <div class="mx-4">
                Is Active
            </div>
        </div>
    </div>    
    <div class="pb-10 flex justify-around">
        <Button text="Close"/>
        <Button text="Update"/>
    </div>
</form>