<script>
    export let name;
    export let type;
</script>

<div class="mx-2">
    <label for={name} class="sr-only">{name}</label>
    <input id={name} v-model={name} name={name} type={type} autocomplete={name} required class="appearance-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-lg focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm my-4" placeholder={name} />
</div>