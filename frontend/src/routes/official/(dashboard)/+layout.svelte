<div class="container min-h-screen flex p-10">
    <div class="w-1/4 pr-4">
        <div>
            <img src="https://avatars.githubusercontent.com/u/59198907?v=4" alt="" srcset="" class=" w-72 rounded-full">
        </div>
        <div class="font-bold text-2xl mt-6">
            Mufassir Ahmad Chowdhury
        </div>
        <div class="font-light text-gray-600 text-xl">
            Mufassir-Chowdhury
        </div>
        <div class="font-light text-gray-600">
            Transport Department Official
        </div>
        <a href="/edit/Official">
            <button type="submit" class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 mt-6">
                Edit Profile
            </button>
        </a>
    </div>
    <div class="w-3/4 border-l-2">
        <div class="w-full flex border-b-2">
            <a href="/bus">
                <div class="my-2 py-1 px-3 hover:bg-gray-200 rounded-md">Buses</div>
            </a>
            <a href="/route">
                <div class="my-2 py-1 px-3 hover:bg-gray-200 rounded-md">Routes</div>
            </a>
            <a href="/stoppage">
                <div class="my-2 py-1 px-3 hover:bg-gray-200 rounded-md">Stoppages</div>
            </a>
            <a href="/demand">
                <div class="my-2 py-1 px-3 hover:bg-gray-200 rounded-md">Demands</div>
            </a>
            <a href="/suggestion">
                <div class="my-2 py-1 px-3 hover:bg-gray-200 rounded-md">Suggestions</div>
            </a>
        </div>
        <slot/>
    </div>
</div>