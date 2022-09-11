<script>
	import Selection from './../../lib/selection.svelte';
import Input from "../../lib/input.svelte";
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
            <button type="submit" class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
            <span class="absolute left-0 inset-y-0 flex items-center pl-3">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-indigo-500 group-hover:text-indigo-400" viewBox="0 0 20 20" fill="currentColor">
                    <path fill-rule="evenodd" d="M5 9V7a5 5 0 0110 0v2a2 2 0 012 2v5a2 2 0 01-2 2H5a2 2 0 01-2-2v-5a2 2 0 012-2zm8-2v2H7V7a3 3 0 016 0z" clip-rule="evenodd" />
                </svg>
            </span>
            Sign in
            </button>
        </div>
        </form>
    </div>
</div>