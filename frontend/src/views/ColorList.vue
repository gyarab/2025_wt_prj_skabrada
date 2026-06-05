<template>
    <h2>Color List</h2>
</template>

<script setup>


    async function load() {
        const url = new URL('/api/Color', window.location.origin)
        const res = await fetch(url)
        if (!res.ok) throw new Error(`HTTP ${res. status}`)
        const data = await

    }


</script>

<template>
    
</template>