<script>
    export let data;
	import Selection from '$lib/selection.svelte';
    import Input from "$lib/input.svelte";
    import Button from '$lib/button.svelte';
    const stoppages = [
        'SUST Gate',
        'Amberkhana',
        'Tilagor'
    ]

</script>
<div class="flex items-center justify-center bg-gray-50 px-4 sm:px-6 lg:px-8">
    <div class="max-w-md w-full">
        <form class="mt-8 space-y-6">
        <input type="hidden" name="remember" value="true" />
        <div class="rounded-md shadow-sm -space-y-px">
            <Input name="Full Name" type="text"/>
            <Input name="ID Number" type="number"/>
            <Input name="Contact Number" type="tel"/>
            {#if data.role == "Student"}
                <Input name="Department" type="text"/>
                <Input name="Batch Number" type="text"/>
                <Input name="Section" type="text"/>
            {:else if data.role == "Teacher"}
                <Input name="Department" type="text"/>
                <Input name="Code Name" type="text"/>
                <Input name="Designation" type="text"/>
            {/if}
            <Selection name="Roles" items={null} disabled={false} selected={data.role}/>
            <Selection name="Stoppages" items={stoppages}/>
            <Input name="Username" type="text"/>
            <Input name="Password" type="password"/>
        </div>    
        <div class="pb-10 flex justify-around">
            <div>
                <a href="/user/bus">
                    <Button text="Go back" type="Button"/>
                </a>
            </div>
            <div>
                <Button text="Update"/>
            </div>
        </div>
        </form>
    </div>
</div>