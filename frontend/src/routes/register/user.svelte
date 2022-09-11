<script>
	import Selection from './../../lib/selection.svelte';
import Input from "../../lib/input.svelte";
import Button from '../../lib/button.svelte';
const roles = [
    'Student',
    'Teacher',
    'Staff'
]
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
            <Selection name="Roles" items={roles}/>
            <Selection name="Stoppages" items={stoppages}/>
            <Input name="Username" type="text"/>
            <Input name="Password" type="password"/>
        </div>    
        <div class="pb-10">
            <Button text="Sign Up"/>
        </div>
        </form>
    </div>
</div>