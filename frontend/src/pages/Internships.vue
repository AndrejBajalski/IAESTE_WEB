]<script setup>
    import { router } from '@/routing/router'
    import { ApiService } from '@/services/api'
    import { onMounted } from 'vue'
    import { ref } from 'vue'

    const apiService = new ApiService()
    const allInternships = ref([])
    onMounted(async () => {
        try {
            allInternships.value = await apiService.getInternships()
            console.log('Fetched internships:', allInternships.value)
        }catch (error) {
            console.error('Error fetching internships:', error)
        }
    })
    const handleAction = (internship) => {
        console.log(`Internship ${internship.referent_number} selected!`)
        router.push({
            name: 'ApplyForm',
            params: {id: internship.id},
            state: {internship: internship}
        })
    }
</script>


<template>
    <h1>All internships:</h1>
    <div>
        <table class="internships-table">
            <thead>
                <tr>
                    <th>Reference Number</th>
                    <th>Employer</th>
                    <th>Field</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
            <tr class="internship-row" v-for="internship in allInternships" :key="internship.id">
                <td><strong>{{ internship.referent_number ?? '--' }}</strong></td>
                <td>{{ internship.company.name ?? '--'}}</td>
                <td>{{ internship.field ?? '--'}}</td>
                <td style="text-align: center;"><button @click="() => handleAction(internship)" class="actions-button">Apply</button></td> 
            </tr>
            </tbody>
        </table>
    </div>
</template>


<style>
    .internships-table {
        border: 1px solid #0b3d59;
        margin: 10px;

        width: 100%;
    }
    .internships-table thead{
        background-color: #0b3d59;
        color: white;
        font-size: 1.2rem;
    }
    .internships-table th{
        padding: 1rem;
    }
    .internship-row td{
        padding: 1rem;
    }
    .internship-row:nth-child(even) {
        background-color: #f2f2f2;
    }
    .actions-button{
        background-color: #0b3d59;
        color: white;
        font-size: 1.1rem;
        border: none;
        padding: 0.5rem 1rem;
        cursor: pointer;
        border-radius: 5px;
    }
</style>