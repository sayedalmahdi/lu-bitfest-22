<script>
import Input from "../../lib/input.svelte";

</script>
<div class="container bg-slate-600 flex flex-row p-16">
    <div class="w-1/2 flex bg-slate-500 items-center justify-center">
        <p class="font-extrabold text-4xl md:text-6xl text-black">
            <span class="text-pink-500"> MAC </span><span class="text-indigo-600"> TIMUM</span>
        </p>
    </div>
    <div class="w-1/2 bg-white">
        <div class="min-h-screen flex items-center justify-center bg-gray-50 px-4 sm:px-6 lg:px-8">
            <div class="max-w-md w-full space-y-8">
              <div>
                <h2 class="mt-6 text-center text-3xl font-extrabold text-gray-900">
                  Sign in to your account
                </h2>
              </div>
              <form class="mt-8 space-y-6">
                <input type="hidden" name="remember" value="true" />
                <div class="rounded-md shadow-sm -space-y-px">
                  <Input name="Username" type="text"/>
                  <Input name="Password" type="password"/>
                </div>
        
                <div class="flex items-center justify-between">
                  <div class="text-sm">
                    <a href="/register" class="font-medium text-indigo-600 hover:text-indigo-500">
                      Register an Account
                    </a>
                  </div>
        
                  <div class="text-sm">
                    <a href="#" class="font-medium text-indigo-600 hover:text-indigo-500">
                      Forgot your password?
                    </a>
                  </div>
                </div>
        
                <div>
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
    </div>
</div>