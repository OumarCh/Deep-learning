<template>
  <div class="small">
    <div>
      <b-form-file browse-text="Upload your dog image" v-model="file" ref="file-input" class="mb-2"></b-form-file>
    </div>
    <button class="btn mt-3 btn-dark">Go</button>

  </div>
</template>

<script>
import axios from 'axios'

export default {
  components: {

  },
  data () {
    return {
      datacollection: null,
      file: null
    }
  },
  mounted () {

    const headers = {
      'Access-Control-Allow-Origin' : '*',
      'Access-Control-Allow-Methods' : 'GET,PUT,POST,DELETE,PATCH,OPTIONS',
    }

    axios.get('http://127.0.0.1:5000/top_ten_gold', {headers}).then((response) => {
          this.data = response.data.Medal;

          const labels = Object.keys(response.data.Medal);
          const values = Object.values(response.data.Medal);

          this.datacollection = {
            labels: labels,
            datasets: [
              {
                label: 'Top Ten Gold Medals',
                backgroundColor: ["#41B883", "#E46651", "#00D8FF","#711183", "#563619", "#b9cec2","#ced69e","#a9cfe5","#f7ef07","#af422f"],
                data: values
              }
              ]

          }
      })
  }
}
</script>

<style>
.small {
  max-width: 600px;
  margin:  150px auto;
}
</style>