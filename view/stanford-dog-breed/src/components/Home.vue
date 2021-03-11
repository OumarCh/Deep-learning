<template>
  <section>

    <Navbar/>

    <div class="container mb-5" >
        <h3>Stanford Dog breed classification</h3>
    </div>

    <div class="tl text-left" >
      <h4>Transfert Learning</h4>
      <p>
        Description de ce qu'on a utilisé <br>
        Graphe accuracy + loss
      </p>
    </div>

    <div class="cnn text-left" >
      <h4>Convolution Neural Network</h4>
      <p>
        Description de ce qu'on a utilisé <br>
        Graphe accuracy et val_accurracy <br>

        Graphe los et val_loss <br>

        Augmentation de données

        etc..
      </p>

    </div>

  </section>
</template>

<script>
import Navbar from "@/components/NavBar";
export default {
  name: 'Home',
  components: {Navbar}
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.container{
  margin-top: 150px;
}
/*h4{
  color: var(--app-primary-color);
}*/
</style>
