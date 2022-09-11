<script>
    import Admin from "./admin.svelte";
    import User from "./user.svelte";
    let activeTabValue = 1;

    let items = [
        { label: "User",
        value: 1,
        component: User
        },
        { label: "Admin",
            value: 2,
            component: Admin
            },
    ];

    const handleClick = tabValue => () => (activeTabValue = tabValue);
</script>

<div class="container min-h-screen bg-slate-600 flex flex-row p-16">
<div class="w-1/2 flex bg-slate-500 items-center justify-center">
    <p class="font-extrabold text-4xl md:text-6xl text-black">
        Sign Up
    </p>
</div>
<div class="w-1/2 bg-white">
    <div class="mt-10 mx-10">
        Register as
    </div>
    <div class="flex items-center justify-evenly">
        {#each items as item}
        <button on:click={handleClick(item.value)} class="group relative flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
            {item.label}
        </button>
        {/each}
    </div>
        {#each items as item}
            {#if activeTabValue == item.value}
            <div class="box">
                <svelte:component this={item.component}/>
            </div>
            {/if}
        {/each}
    </div>
</div>