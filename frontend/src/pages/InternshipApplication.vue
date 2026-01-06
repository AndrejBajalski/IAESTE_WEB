<script setup>
import { ApiService } from '@/services/api';
import { ref, onMounted } from 'vue';

    const props = defineProps({ id: String })
    const internship = ref(null)
    const apiService = new ApiService();
    onMounted(async () => {
        try {
            const response = await apiService.getInternshipById(props.id)
            internship.value = response;
            console.log("Internship data: ", response)
        } catch (error) {
            console.error("Could not load internship details", error)
        }
    });
    const candidateName = ref('')
    const candidateSurname = ref('')
    const candidateFaculty = ref('')
    const didApply = ref(false)

    const handleSubmit = async () => {
        const candidateData = {name: candidateName.value, surname: candidateSurname.value, faculty: candidateFaculty.value}
        try{
            await apiService.applyForInternship(props.id, candidateData)
            console.log("Successfully created application for ", candidateData.name, candidateData.surname)
            didApply.value = true
        }
        catch(error){
            console.error("Failed applying for internship", error)
        }
    }
</script>

<template>
    <h1>Send your internship application</h1>
    <div>
        <p v-if="didApply" class="bg-success">Successfully applied!</p>
        <p>Referent number: {{ internship?.referent_number ?? '--' }}</p>
        <p>Employer: {{ internship?.company?.name ?? '--' }}</p>
        <p>Job description:</p>
        <p>{{ internship?.description ?? '--' }}</p> 
        <form @submit.prevent="handleSubmit" >
            <label for="name">Name:</label><br>
            <input type="text" id="name" name="name" v-model="candidateName"><br>
            <label for="surname">Surname:</label><br>
            <input type="text" id="surname" name="surname" v-model="candidateSurname"><br>
            <label for="faculty">Faculty:</label><br>
            <input type="text" id="faculty" name="faculty" v-model="candidateFaculty"><br>
            <button type="submit">Apply</button>
        </form>
    </div>
</template>