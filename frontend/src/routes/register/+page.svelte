<script>
    import { text } from "svelte/internal";
import Button from "../../lib/button.svelte";
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
        <Button onClick={handleClick(item.value)} text={item.label} />
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