<template>
  <nav class="navbar">
    <div class="nav-logo">IAESTE Web</div>
    <ul class="nav-links">
        <li><router-link :to="{name: 'Home'}">Home</router-link></li>
        <li><router-link :to="{name: 'Internships'}">Internships</router-link></li>
        <li><router-link :to="{name: 'AllApplications'}">Applications</router-link></li>
    </ul>
  </nav>
</template>

<style scoped>
.navbar {
  display: flex;
  /* justify-content: space-between; */
  align-items: center;
  padding: 1rem 2rem;
  background-color: #0b3d59;
  color: white;
  font-family: Arial, Helvetica, sans-serif
}

.nav-logo {
    font-size: 1.2rem;
}

.nav-links {
  display: flex;
  width: 100%;
  justify-content: center;
  list-style: none;
  gap: 3rem;
}

.nav-links a {
  color: white;
  text-decoration: none;
}

/* Style for the active page */
.router-link-active {
  font-weight: bold;
}
</style>