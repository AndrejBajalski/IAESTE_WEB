<script setup>
    import { router } from '@/routing/router'
    import { ApiService } from '@/services/api'
    import { onMounted } from 'vue'
    import { ref } from 'vue'

    const apiService = new ApiService()
    const allApplications = ref([])
    onMounted(async () => {
        try {
            allApplications.value = await apiService.getApplications()
            console.log('Fetched internship applications:', allApplications.value)
        }catch (error) {
            console.error('Error fetching internship applications:', error)
        }
    })
</script>

<template>
    <h1>All applications</h1>
    <div class="applications-container">
        <div v-for="(application, i) in allApplications" :key="i" class="application">
            <div>
                <h3>Internship</h3>
                <p>Reference Number: {{ application.internship.referent_number }}</p>
                <p>Employer: {{ application.internship.company.name }}</p>
                <p>Location: {{ application.internship.company.city }}, {{ application.internship.company.country }}</p>
                <p>Field: {{ application.internship.field }}</p>
            </div>
            <div>
                <h3>Applicant info</h3>
                <p>{{ application.candidate.name}} {{ application.candidate.surname }}</p>
                <p>Student at {{ application.candidate.faculty }}</p>
            </div>
        </div>
    </div>
</template>

<style>
    .applications-container{
        display: flex;
        width: 100%;
        /* justify-content: center; */
    }
    .application{
        display: flex;
        gap: 4rem;
        justify-content: space-between;
        padding: 2rem;
        border: 2px solid #0b3d59;
        border-radius: 5px;
    }

</style>