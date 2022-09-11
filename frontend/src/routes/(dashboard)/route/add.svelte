<script>
    import Input from "../../../lib/input.svelte";
    import Button from "../../../lib/button.svelte";
</script>

<form class="mt-8 space-y-6">
    <input type="hidden" name="remember" value="true" />
    <div class="rounded-md shadow-sm -space-y-px">
        <Input name="Start Location" type="text"/>
        <Input name="Start Lattitude" type="text"/>
        <Input name="Start Longitude" type="number"/>
        <Input name="Start Time" type="time"/>
    </div>    
    <div class="pb-10 flex justify-around">
        <Button text="Close"/>
        <Button text="Add Route"/>
    </div>
</form>