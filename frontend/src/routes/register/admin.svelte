<script>
import Button from "../../lib/button.svelte";
import Input from "../../lib/input.svelte";

</script>
<div class="flex items-center justify-center bg-gray-50 px-4 sm:px-6 lg:px-8">
    <div class="max-w-md w-full">
        <form class="mt-8 space-y-6">
        <input type="hidden" name="remember" value="true" />
        <div class="rounded-md shadow-sm -space-y-px">
            <Input name="Full Name" type="text"/>
            <Input name="Contact Number" type="tel"/>
            <Input name="Username" type="text"/>
            <Input name="Password" type="password"/>
        </div>    
        <div>
            <Button text="Sign Up"/>
        </div>
        </form>
    </div>
</div>