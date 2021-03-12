<template>
  <section>

    <Navbar/>

    <div class="container mb-5" >
        <h3>Stanford Dog breed classification</h3>
    </div>

    <div class="tl text-left" >
      <h4>Transfert Learning</h4>

       Nous avons utilisé l'algorithme MobileNetV2
        <br>
        Traitement :
        <ul>
          <li>image_dataset</li>
          <li>optimizer: adam</li>
          <li>loss: categorical_crossentropy</li>
          <li>etc</li>
        </ul>
      Graphique accuracy:
      <br>
      <img src="../assets/images/acc_tl.png" />
      <br>
      Graphique loss:
      <br>
      <img src="../assets/images/loss_tl.png" />
      <br>
    </div>

    <div class="cnn text-left" >
      <h4>Convolution Neural Network</h4>

      <br>
      Traitement :
      <ul>
        <li>image processing : rescale</li>
        <li>Dropout</li>
        <li>optimizer: adam</li>
        <li>loss: categorical_crossentropy</li>
        <li>etc</li>
      </ul>
      <h5>Avec 20 epochs</h5>
      Graphique accuracy:
      <br>
      <img src="../assets/images/acc_brut_20ep.png" />
      <br>
      Graphique loss:
      <br>
      <img src="../assets/images/loss_brut__20ep.png" />
      <br>

      <h5>Avec 15 epochs - Dropout</h5>
      Graphique accuracy:
      <br>
      <img src="../assets/images/acc_drop.png" />
      <br>
      Graphique loss:
      <br>
      <img src="../assets/images/loss_drop.png" />
      <br>

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
