]<script setup>
    import { ApiService } from '@/services/api'
    import { onMounted } from 'vue'
    import { ref } from 'vue'

    const apiService = new ApiService()
    const allInternships = ref([])
    // onMounted(async () => {
    //     try {
    //         allInternships.value = await apiService.getInternships()
    //         console.log('Fetched internships:', allInternships.value)
    //     }catch (error) {
    //         console.error('Error fetching internships:', error)
    //     }
    // })
</script>


<template>
    <h1>All internships:</h1>
    <div>
        <!-- <div class="internship-container" v-for="internship in allInternships" :key="internship.id">
            <h4>{{ internship.referent_number }}</h4>
            <div>{{ internship.company.name }}</div>
            <div>{{ internship.field }}</div> 
        </div> -->
    </div>
</template>


<style>
.internship-container {
    border: 1px solid #0B3959;
    margin: 10px;
    padding: 1rem;
    display: flex;
    justify-content: space-around;
}
</style>