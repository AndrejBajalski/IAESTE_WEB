import axios from 'axios';

class ApiService {
    constructor(baseURL=import.meta.env.VITE_API_BASE_URL){
        this.baseURL = baseURL
        console.log("API BASE URL SET TO: ", this.baseURL)
    }
    
    async get(endpoint, params = {}) {
        const url = this.baseURL + endpoint
        return axios.get(url)
                    .then(response => response.data)
                    .catch(error => console.log('Error fetching data from API:', error ))
    }
    async getInternships(params = {}) {
        const url = this.baseURL + "/api/internships"
        return axios.get(url)
                    .then(response => response.data)
                    .catch(error => console.log('Error fetching data from API:', error ))
    }
    async getInternshipById(id) {
        const url = this.baseURL + `/api/internships/${id}`
        return axios.get(url)
                    .then(response => response.data)
                    .catch(error => console.log('Error fetching data from API:', error ))
    }
    async getApplications() {
        const url = this.baseURL + `/api/applications`
        return axios.get(url)
                    .then(response => response.data)
                    .catch(error => console.log('Error fetching data from API:', error ))
    }
    async applyForInternship(internshipId, applicantData) {
        const url = this.baseURL + `/api/applications`
        return axios.post(url, {
            internship: internshipId,
            candidate: applicantData
        }).then(response => response.data)
          .catch(error => console.log('Error submitting application to API:', error))
    }
}

export { ApiService };