<script>
	import Button from './../../lib/button.svelte';
import Input from "../../lib/input.svelte";
  let username = null;
  let password = null;
  let result = null
  let result2 = null

  async function login(){
		const response = await fetch('https://9fea-163-47-36-254.ap.ngrok.io/auth/login/', {
			method: 'POST',
      headers: {
				'Accept': 'application/json',
        "Content-Type": "application/x-www-form-urlencoded"
			},
      body: `username=${username}&password=${password}`
      // body: `username=abcdef&password=okay12no`
		})
    const json = await response.json()
    console.log(json.key)
    result = JSON.stringify(json)
    console.log(result)
    const res = await fetch('https://9fea-163-47-36-254.ap.ngrok.io/api/accounts/user/', {
			method: 'GET',
      headers: {
        'Authorization': `token ${json.key}`,
        'Content-Type': 'application/json'
			},
		})
    // json = await response.json()
    // result2 = JSON.stringify(json)
    // console.log(result2)
  }
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
              <form class="mt-8 space-y-6 " on:click|preventDefault>
                <input type="hidden" name="remember" value="true" />
                <div class="rounded-md shadow-sm -space-y-px">
                  
                  <div class="mx-2">
                    <label for="UserName" class="sr-only">"UserName"</label>
                    <input id="UserName" bind:value={username} v-model="UserName" name="UserName" type="text" autocomplete="UserName" required class="appearance-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-lg focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm my-4" placeholder="UserName" />
                  </div>
                  <div class="mx-2">
                    <label for="password" class="sr-only">"password"</label>
                    <input id="password" bind:value={password}  name="password" type="password" autocomplete="password" required class="appearance-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-lg focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm my-4" placeholder="Password" />
                  </div>
                <!-- {password} -->
                  <!-- <Input name="Username" type="text"/>
                  <Input name="Password" type="password"/> -->
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
                  <button on:click={login} type="submit" class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
                    Sign in
                  </button>
                  <!-- <Button text="Sign in"/> -->
                  {result}
                  {result2}
                </div>
              </form>
            </div>
        </div>
    </div>
</div>